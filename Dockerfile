FROM golang:1.21.0

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go mod  files
COPY go.mod ./

# Download all dependencies.
RUN go mod download

# Copy the source code into the container
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -o /go-docker-app

# Expose port 8080 
EXPOSE 8080

# Command to run the executable
CMD ["/go-docker-app"]
