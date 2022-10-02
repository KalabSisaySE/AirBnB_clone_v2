#!/usr/bin/python3
"""the `3-deploy_web_static` module
defines the function `deploy`
"""
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


def deploy():
    """packs `web_static` and deploys it on the servers"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
