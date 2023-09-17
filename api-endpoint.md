# BD Smart School Management

**Namespaces**

- Public - Anyone with the API access
- Admin / Private - Internal use only (restricted, different CORS policy)

**We will follow no namespace at this moment**

- [ ] Institutes
  - [ ] Get all teachers
    - Method: GET
    - Access: Public
    - Path: /institutes

    - Response
      - 200
        - institute data
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

- Teachers
    - Get all teachers
        
        Method: GET
        
        Access: Public
        
        Path: /teachers?query=params
        
        Query:
        
        - page (default 1) - current page number
        - limit (default 10) - the number of objects should be returned
        - sortType (default desc) - the type of sort, it could be either asc or desc
        - sortBy (default updatedAt) - the property that will used to sort. It could be either updatedAt or title.
        - search - the search term to filter articles based on the titles.
        
        Response:
        
        - 200
            - teacher data
                - id
                - title
                - cover
                - author
                    - id
                    - name
                - timestamp
                - links
            - pagination
                - page
                - limit
                - nextPage
                - prevPage
                - totalPage
                - totalArticle
            - links
                - self
                - nextPage
                - prevPage
        - 400
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
