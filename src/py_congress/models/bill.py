from pydantic import BaseModel, StrictInt, StrictStr, HttpUrl

class BillListInfo:
    """Returned model for methods interfacing with the following endpoints:
            - /bill
            - /bill/:congress
            - /bill/:congress/:billType
    """
    congress: int

    class latestAction:
        actionDate: str #TODO: put datetime validator and type for this. Ex: "2022-04-06"
        text: str
    latestAction: latestAction
    number: str #TODO: validator for this to be checked as a number. Ex: "3076"
    originChamber: str #TODO: Check for potential enum
    originChamberCode: str #TODO: Check for potential enum
    title: str
    type: str #TODO: Check for potential enum
    updateDate: str #TODO: put datetime validator and type for this. Ex: "2022-09-29"
    updateDateIncludingText: str #TODO: put datetime validator and type for this. Ex: "2022-09-29T03:27:05Z"
    url: HttpUrl

class BillDetailedInfo:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber
    """
    ...

class BillActions:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:actions
    """
    ...

class BillAmendments:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:ammendments
    """
    ...

class BillCommittees:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:committees
    """
    ...

class BillCosponsors:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:cosponsors
    """
    ...

class BillRelatedBills:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:relatedbills
    """
    ...

class BillSubjects:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:subjects
    """
    ...

class BillSummaries:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:summaries
    """
    ...

class BillText:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:text
    """
    ...

class BillTitles:
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:titles
    """
    ...