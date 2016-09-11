# orcidchecksum

This repo is basically two scripts:

## generateCheckDigit()
A python implementation of the ORCID checksum algorithm.  This is used to generate the final digit of an ORCID upon assignment.  For more information, see the ORCID website:  http://support.orcid.org/knowledgebase/articles/116780-structure-of-the-orcid-identifier

## generateAllPossibleORCID.py
Basically exactly what the title says.  Populates a sqlite3 db (db/allpossibleORCIDs.db) with just over half a GB of numbers.
