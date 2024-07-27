import asyncio
import json
import logging

from lamini.api.rest_requests import make_async_web_request

logger = logging.getLogger(__name__)


async def process_batch(args):
    client = args["client"]
    key = args["key"]
    api_prefix = args["api_prefix"]
    batch = args["batch"]
    reservation_api = args["reservation_api"]
    url = api_prefix + "completions"
    # this will block until there is space in capacity
    await reservation_api.async_pause_for_reservation_start()

    def can_submit_query():
        if reservation_api.current_reservation is None:
            return True
        if reservation_api.capacity_remaining < len(batch["prompt"]):
            return False
        # Now we can consume credits and send batch
        reservation_api.update_capacity_use(len(batch["prompt"]))
        logger.debug(
            f"yes reservation_api.capacity_remaining {reservation_api.capacity_remaining}"
        )
        return True

    if not can_submit_query():
        async with reservation_api.condition:
            await reservation_api.condition.wait_for(can_submit_query)

    # Separate thread updates existing reservations
    if reservation_api.current_reservation is not None:
        batch = {
            "reservation_id": reservation_api.current_reservation["reservation_id"],
            **batch,
        }

    logger.debug(f"Sending batch {args['index']}")
    result = await make_async_web_request(client, key, url, "post", batch)
    logger.debug(f"Received batch response")
    reservation_api.update_capacity_needed(len(batch["prompt"]))
    logger.debug(f"reservation_api.capacity_needed {reservation_api.capacity_needed}")
    if (
        reservation_api.capacity_needed > 0
        and reservation_api.capacity_remaining < len(batch["prompt"])
        and not reservation_api.is_polling
    ):
        logger.debug(
            f"capacity remaining after query: {reservation_api.capacity_remaining}"
        )
        reservation_api.poll_for_reservation.set()

    return result
