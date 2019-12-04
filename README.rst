CanDIG Schemas
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The CanDIG schemas has been built on the  `ga4gh-schemas <https://github.com/ga4gh/ga4gh-schemas>`_
with extended schema definitions on metadata, complex search requests formats, etc. It defines the data
schemas, requests formats that are accepted by the `candig-server <https://github.com/candig/candig-server>`_

To learn more about the CanDIG project or to contact us, please visit https://www.distributedgenomics.ca.

To compile the schemas, first make sure you have `protoc` (3.3.0) install, change the source schema
under ``src/candig``. Then go to the ``scripts`` directory, and run

``python process_schemas.py 1.0.0``

Note that you can only run the script when you are under the ``scripts`` directory. In the example
above, ``1.0.0`` is the protocol version.