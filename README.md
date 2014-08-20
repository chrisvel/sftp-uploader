Sftp remote site uploader
=================================================================

This software checks for files in a local folder on a frequent basis and then uploads them to a remote Sftp site.


Installation and requirements
-----------------------------

- Python 3.3
- tkinter
- logging
- pycrypto 2.6 for python 3.3
- paramiko
- ecdsa

Installation of an appropriate pycrypto version is needed prior to running the script.

Usage
-----

The software has been setup to upload Sftp files on a remote location and make all the necessary security checks to complete.

    python main.py

#TODO Write a complete description of all actions taken after script execution.

License
-------
::
    Copyright (c) 2014 chrisvel

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
