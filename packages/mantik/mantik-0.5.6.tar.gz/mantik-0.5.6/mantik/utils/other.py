import contextlib
import os


@contextlib.contextmanager
def temp_chdir(path: str):
    _old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(_old_cwd)


def construct_git_clone_uri(
    uri: str, git_access_token: str, platform: str
) -> str:
    # How github expects the URI to look like for cloning
    if platform == "GitLab":
        uri = uri.replace("https://", f"https://oauth:{git_access_token}@")
    else:  # GitHub
        uri = uri.replace("https://", f"https://{git_access_token}@")
    return uri
