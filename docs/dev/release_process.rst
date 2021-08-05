Release Process
===============

For maintainers only:

- Update ``CHANGELOG.md`` with the version changes
- Update ``docs/`` as required
- Update ``README.md`` as required
- Commit changes
- Run ``bump2version <major|minor|patch>`` to update the version number (pick one of the options)

    - Version number on ``pyproject.toml`` will be updated automatically
    - You can specify the ``--new_version`` flag in case you wish to manually set the newest version (if not provided, it will be done automatically based on the chosen option)
    - The command also creates a git tag

- Run ``poetry build`` to package the new version artifacts
- Run ``poetry publish`` to publish the packages