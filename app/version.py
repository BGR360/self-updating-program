from pbr.version import VersionInfo

info = VersionInfo('self_updating_app').semantic_version()
__version__ = info.release_string()
version_info = info.version_tuple()
