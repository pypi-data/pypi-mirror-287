# Dvinci API Documentation

## Table of Contents

- [Dvinci API Documentation](#dvinci-api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Endpoints](#endpoints)
    - [Applications](#applications)
      - [/applications/](#applications-1)
        - [GET](#get)
        - [POST](#post)
      - [/applications/?externalId={externalId}](#applicationsexternalidexternalid)
        - [GET](#get-1)
      - [/applications/{id}](#applicationsid)
        - [GET](#get-2)
        - [PUT](#put)
      - [/applications/{id}/delete](#applicationsiddelete)
        - [POST](#post-1)
      - [/applications/{id}/statusChange/{statusId}](#applicationsidstatuschangestatusid)
        - [POST](#post-2)
      - [/applications/{id}/jobOpeningMove/{jobOpeningId}](#applicationsidjobopeningmovejobopeningid)
        - [POST](#post-3)
      - [/applications/{id}/attachmentsget](#applicationsidattachmentsget)
        - [GET](#get-3)
        - [POST](#post-4)
      - [/applications/{id}/attachments/{attachmentId}](#applicationsidattachmentsattachmentid)
        - [GET](#get-4)
      - [/applications/{id}/attachments/{attachmentId}/pdf](#applicationsidattachmentsattachmentidpdf)
        - [GET](#get-5)
      - [/applications/{id}/attachments/{attachmentId}/delete](#applicationsidattachmentsattachmentiddelete)
        - [POST](#post-5)
      - [/applications/{id}/history](#applicationsidhistory)
        - [GET](#get-6)
        - [PUT](#put-1)
      - [/applications/{id}/history/{externalId}](#applicationsidhistoryexternalid)
        - [PUT](#put-2)
      - [Configuration](#configuration)
      - [Hiring requests](#hiring-requests)
      - [Job openings](#job-openings)
      - [Job publications](#job-publications)
      - [Job publication placements](#job-publication-placements)
      - [Job publication channels](#job-publication-channels)
      - [Locations](#locations)
      - [Onboardings](#onboardings)
      - [Organisation units](#organisation-units)
      - [Persons](#persons)
      - [Users](#users)
      - [User groups](#user-groups)

## Endpoints

### Applications

#### /applications/

##### GET

Get a list of permitted applications.

##### POST

Create a new application.

#### /applications/?externalId={externalId}

##### GET

Get a application by external id.

#### /applications/{id}

##### GET

Get a specific application.

##### PUT

Update a specific application.

#### /applications/{id}/delete

##### POST

Delete a specific application.

#### /applications/{id}/statusChange/{statusId}

##### POST

Change status for a specific application.

#### /applications/{id}/jobOpeningMove/{jobOpeningId}

##### POST

#### /applications/{id}/attachmentsget

##### GET

##### POST

#### /applications/{id}/attachments/{attachmentId}

##### GET

#### /applications/{id}/attachments/{attachmentId}/pdf

##### GET

#### /applications/{id}/attachments/{attachmentId}/delete

##### POST

#### /applications/{id}/history

##### GET

##### PUT

#### /applications/{id}/history/{externalId}

##### PUT

#### Configuration

#### Hiring requests

#### Job openings

#### Job publications

#### Job publication placements

#### Job publication channels

#### Locations

#### Onboardings

#### Organisation units

#### Persons

#### Users

#### User groups
