from producer import send_message
from data import interesting_data, not_interesting_data

TOPIC_INTERESTING = "interesting"
TOPIC_NOT_INTERESTING = "not_interesting"


interesting_idx = {cat: 0 for cat in interesting_data.keys()}
not_interesting_idx = {cat: 0 for cat in not_interesting_data.keys()}

async def publish_one_message_per_category():
    """Send one message per category for interesting and not interesting"""
    # Interesting
    for cat, data_list in interesting_data.items():
        idx = interesting_idx[cat] % len(data_list)
        message = {"category": cat, "content": data_list[idx]}
        await send_message(TOPIC_INTERESTING, message)
        interesting_idx[cat] += 1

    # Not interesting
    for cat, data_list in not_interesting_data.items():
        idx = not_interesting_idx[cat] % len(data_list)
        message = {"category": cat, "content": data_list[idx]}
        await send_message(TOPIC_NOT_INTERESTING, message)
        not_interesting_idx[cat] += 1
