# BD Smart School Management

**Namespaces**

- Public - Anyone with the API access
- Admin / Private - Internal use only (restricted, different CORS policy)

**We will follow no namespace at this moment**

- [ ] Institutes
  - [ ] Get all institutes
    - Method: GET
    - Access: Public
    - Path: /institutes

    - Response
      - 200
        - data
          - id
          - name
          - established_year
          - president
          - principal
          - website_domain_address
          - email
          - address
          - phone_number_1
          - phone_number_2
          - image
          - logo
          - description
          - eiin_number
          - institute_code
          - type
      - 400
        - message
      - 500
        - message
  - [ ] Get Single institutes
    - Method: GET
    - Access: Public
    - Path: /institutes/id

    - Response
      - 200
        - data
          - id
          - name
          - established_year
          - president
          - principal
          - website_domain_address
          - email
          - address
          - phone_number_1
          - phone_number_2
          - image
          - logo
          - description
          - eiin_number
          - institute_code
          - type
      - 404
        - message
      - 400
        - message
  - [ ] Update an institutes using put
    - Method: PUT
    - Access: Private
    - Path: /institutes/id
    - Payload
        - name
        - established_year
        - president
        - principal
        - website_domain_address
        - email
        - address
        - phone_number_1
        - phone_number_2
        - image
        - logo
        - description
        - eiin_number
        - institute_code
        - type

    - Response
      - 200
        - message
        - institute data 
      - 400
        - message
        - data (Array of error messages)
          - field
          - message
      - 404
        - message
      - 401
        - message
  - [ ] Update an institutes using patch
    - Method: PATCH
    - Access: Private
    - Path: /institutes/id
    - Payload
      - name
      - established_year
      - president
      - principal
      - website_domain_address
      - email
      - address
      - phone_number_1
      - phone_number_2
      - image
      - logo
      - description
      - eiin_number
      - institute_code
      - type

    - Response
      - 200
        - message
        - institute data
      - 400
        - message
        - data (Array of error messages)
          - field
          - message
      - 404
        - message
      - 401
        - message
  - [ ] Delete an institute
    Method: Delete
    Access: Private
    Path: /institutes/id
    
    Response:
    - 204
    - 404
        - message
    - 401
        - message

- Klass
    - Get all Klasses
        Method: GET
        Access: Public
        Path: /klasses
        
        Response:
          - 200
              - klass data
                - id
                - institute
                - name
                - seats
                - room_number
                - type
                - timestamp
          - 400
              - message
          - 500
              - message
    - Get Single klass
        Method: GET
        Access: Public
        Path: /klasses/id
        
        Response:
          - 200
            - klass data
          - 404
            - message
          - 500
              - message
        
    - Create a new article
        
        Method: POST
        
        Access: Private
        
        Path: /articles
        
        Request Body:
        
        - title
        - body
        - cover (optional)
        - status (default draft)
        
        Response
        
        - 201
            - message
            - article data
            - links
                - self
                - author
                - comments
        - 400
            - message
            - data (Array of error messages)
                - field
                - message
        - 401
            - message
    - Get a single article
