from rq import get_current_job

from kalabash.core.password_hashers import cache_available_password_hasher


def job_retrieve_available_hashers():
    if get_current_job() is None:
        return
    cache_available_password_hasher()
