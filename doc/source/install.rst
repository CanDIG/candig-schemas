Installing the CanDIG Schemas
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The schemas are documents (text files) that formally describe the
messages that pass between CanDIG servers and clients, which we
also refer to collectively as "the API." The schemas are written in a
language called `Protocol Buffers 3 <https://developers.google.com/protocol-buffers/>`__.

For instructions on how to install Protocol Buffers 3 on your system,
consult the `protocol buffers C++ installation instructions page
<https://github.com/google/protobuf/blob/master/src/README.md>`__.

We use the schemas in a couple of different ways:

- to generate source code
- to generate documentation

Generating Source Code
@@@@@@@@@@@@@@@@@@@@@@

::

$ cd src/main/proto && protoc --python_out=. ga4gh/*

Installing the Documentation Tools and Generating Documentation
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

We use a tool called Sphinx to generate the documentation from Protocol
Buffers input files.

Install prerequisites
#####################

To use the Sphinx/Protocol Buffers documentation generator, you must
install some software packages it requires.

Maven
$$$$$

We use the Maven build tool to control processing the schemas.
Installing Maven will also install Java.

Ubuntu
%%%%%%

::

$ sudo apt-get install maven

CentOS/Fedora
%%%%%%%%%%%%%

::

$ sudo yum install maven

Mac OS X
%%%%%%%%

::

$ brew install maven

Python/PIP
$$$$$$$$$$

We use some Python utility programs also.

Install the Python installer ``pip``.

Ubuntu
%%%%%%

::

$ sudo apt-get install python-pip

CentOS/Fedora
%%%%%%%%%%%%%

::

$ sudo yum install python-pip

Mac OS X
%%%%%%%%

Use ``brew``:

::

$ brew install pip

Or download ``pip`` from `here <https://bootstrap.pypa.io/get-pip.py>`__
and run it:

::

$ python get-pip.py

Putting it all together
$$$$$$$$$$$$$$$$$$$$$$$

Do this once to install all required Python packages:

::

$ sudo pip install -r python/dev_requirements.txt -c python/constraints.txt

Generate the documentation
@@@@@@@@@@@@@@@@@@@@@@@@@@

With those prerequisites out of the way, do this anytime you wish to
generate the documentation.

Assuming your working directory is the base "``schemas``\ " directory,
do this:

::

$ mvn site

The documentation you generate will reside in
``target/generated-docs/merged/html``. To view it, open the file
``target/generated-docs/merged/html/index.html`` in a browser.
