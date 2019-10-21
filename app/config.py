"""Static application configuration is placed here."""

GITHUB_REPO = 'BGR360/self-updating-program'

def github_repo_url():
    return 'https://github.com/{}'.format(GITHUB_REPO)

def github_pypi_package_url(version=None):
    url = 'git+{}.git'.format(github_repo_url())
    if version is not None:
        url += '@{}'.format(version)
    return url

def github_api_url():
    return 'https://api.github.com/repos/{}'.format(GITHUB_REPO)
