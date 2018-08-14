swagger: "2.0"
info:
  title: Weather API
  description: Weather Prediction Web Service
  version: 1.0.0
host: desolate-beyond-76412.herokuapp.com
basePath: /
schemes:
  - https
paths:
  /clima:
    get:
      parameters:
        - in: query
          name: dia
          required: true
      summary: Returns a list of users.
      description: Optional extended description in Markdown.
      produces:
        - application/json
      responses:
        200:
          description: OK
          schema:
            type: object
            properties:
              dia:
                type: integer
                example: 100
              clima:
                type: string
                example: Lluvia
        404:
          description: Resource not found
          schema:
            type: object
            properties:
              error:
                type: string
                example: Resource not found