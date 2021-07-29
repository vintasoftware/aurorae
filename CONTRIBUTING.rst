.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/vintasoftware/vinta-pagamentos/issues

Before reporting a bug, please double-check the requirements: https://github.com/vintasoftware/vinta-pagamentos/blob/main/README.md#requirements

If you think you really found a bug, please create a GitHub issue and use the "Bug report" template.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it. Please comment on the issue saying you're working in a solution.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it. Please comment on the issue saying you're working on a solution.

Write Documentation
~~~~~~~~~~~~~~~~~~~

vinta-pagamentos could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

If you have a suggestion, concern, or want to propose a feature, please create a GitHub issue and use the "New feature" template.

Get Started!
------------

Ready to contribute? Please read our Code of Conduct: https://github.com/vintasoftware/vinta-pagamentos/blob/main/CODE_OF_CONDUCT.md

Now, here's how to set up `vinta-pagamentos` for local development.

1. Fork the `vinta-pagamentos` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/vinta-pagamentos.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv vinta-pagamentos
    $ cd vinta-pagamentos/
    $ poetry install

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the tests::

    $ poetry run pytest

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a Pull Request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a Pull Request, check that it meets these guidelines:

1. The Pull Request should include tests.
2. If the Pull Request adds functionality, the docs should be updated.
3. The CI should pass.
