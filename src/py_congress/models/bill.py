from typing import List, Optional
from pydantic import BaseModel as B, StrictInt, StrictStr, HttpUrl

class BillListInfoItem(B):
    """Returned model for methods interfacing with the following endpoints:
            - /bill
            - /bill/:congress
            - /bill/:congress/:billType
    """
    congress: int

    class LatestAction(B):
        actionDate: str #TODO: put datetime validator and type for this. Ex: "2022-04-06"
        text: str
    latestAction: LatestAction
    number: str #TODO: validator for this to be checked as a number. Ex: "3076"
    originChamber: str #TODO: Check for potential enum
    originChamberCode: str #TODO: Check for potential enum
    title: str
    type: str #TODO: Check for potential enum
    updateDate: str #TODO: put datetime validator and type for this. Ex: "2022-09-29"
    updateDateIncludingText: str #TODO: put datetime validator and type for this. Ex: "2022-09-29T03:27:05Z"
    url: HttpUrl

class BillDetailedInfo(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber
    """
    class Bill(B):
        class Details(B):
            count: int
            url: HttpUrl
        class CboCostEstimatesItem(B):
            description: str
            pubDate: str
            title: str
            url: HttpUrl
        class CommitteeReportsItem(B):
            citation: str
            url: HttpUrl
        class Cosponsors(Details):
            countIncludingWithdrawnCosponsors: int
        class LatestAction(B):
            actionDate: str
            text: str
        class LawsItem(B):
            number: str
            type: str
        class PolicyArea(B):
            name: str
        class SponsorsItem(B):
            bioguideId: str
            district: int
            firstName: str
            fullName: str
            isByRequest: str
            lastName: str
            middleName: str
            party: str #TODO: check for enum
            state: str #TODO: Check for state type?
            url: HttpUrl
            
        actions: Details
        amendments: Details
        cboCostEstimates: List[CboCostEstimatesItem]
        committeeReports: List[CommitteeReportsItem]
        committees: Details
        congress: int
        constitutionalAuthorityStatementText: str
        cosponsors: Cosponsors
        introducedDate: str
        latestAction: LatestAction
        laws: List[LawsItem]
        number: str #TODO: Validator or loose cast to check if str is a number
        originChamber: str
        policyArea: PolicyArea
        relatedBills: Details
        sponsors: List[SponsorsItem]
        subjects: Details
        summaries: Details
        textVersions: Details
        title: str
        titles: Details
        type: str
        updateDate: str
        updateDateIncludingText: str
    bill: Bill

class BillActions(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:actions
    """
    class ActionsItem(B):
        class SourceSystem(B):
            code: int
            name: str
        actionCode: str
        actionDate: str #TODO: Datetime?
        sourceSystem: SourceSystem
        text: str
        type: str
    actions: List[ActionsItem]

class BillAmendments(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:ammendments
    """
    class AmendmentsItem(B):
        class LatestAction(B):
            actionDate: str
            actionTime: str
            text: str
        congress: int
        description: str
        latestAction: LatestAction
        number: str
        type: str
        updateDate: str
        url: HttpUrl
    amendments: List[AmendmentsItem]

class BillCommittees(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:committees
    """
    class CommitteesItem(B):
        class ActivitiesItem(B):
            date: str
            name: str
        activities: List[ActivitiesItem]
        chamber: str
        name: str
        systemCode: str
        type: str
        url: HttpUrl
    committees: List[CommitteesItem]

class BillCosponsors(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:cosponsors
    """
    class CosponsorsItem(B):
        bioguideId: str
        district: int
        firstName: str
        fullName: str
        isOriginalCosponsor: bool
        lastName: str
        middleName: str
        party: str
        sponsorshipDate: str
        state: str
        url: HttpUrl
    cosponsors: List[CosponsorsItem]

class BillRelatedBills(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:relatedbills
    """
    class RelatedBillsItem(B):
        class LatestAction(B):
            actionDate: str
            text: str
        class RelationshipDetailsItem(B):
            identifiedBy: str
            type: str
        congress: int
        latestAction: LatestAction
        number: int
        relationshipDetails: List[RelationshipDetailsItem]
        title: str
        type: str
        url: HttpUrl
    relatedBills: List[RelatedBillsItem]

class BillSubjects(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:subjects
    """
    class SubjectItems(B):
        class LegislativeSubjectsItem(B):
            name: str
        class PolicyArea(B):
            name: str
        legislativeSubjects: List[LegislativeSubjectsItem]
        policyArea: PolicyArea
    subjects: SubjectItems

class BillSummaries(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:summaries
    """
    class SummariesItem(B):
        actionDate: str
        actionDesc: str
        text: str
        updateDate: str
        versionCode: str
    summaries: List[SummariesItem]

class BillText(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:text
    """
    class TextVersionsItem(B):
        class FormatsItem(B):
            type: str
            url: HttpUrl
        date: Optional[str]
        formats: List[FormatsItem]
        type: str
    textVersions: List[TextVersionsItem]

class BillTitles(B):
    """Returned model for methods interfacing with the following endpoints:
        - /bill/:congress/:billType/:billNumber/:titles
    """
    class TitlesItem(B):
        billTextVersionCode: Optional[str]
        billTextVersionName: Optional[str]
        chamberCode: Optional[str]
        chamberName: Optional[str]
        title: str
        titleType: str
    titles: List[TitlesItem]