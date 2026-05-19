default:
    @just --list

backend *cmd:
    @cd backend && just {{cmd}}

cli *cmd:
    @cd cli && just {{cmd}}

frontend *cmd:
    @cd frontend && just {{cmd}}

install:
    @just backend install
    @just cli install
    @just frontend install

all-test:
    @just backend test
    @just cli test
    @just frontend test

all-lint:
    @just backend lint
    @just cli lint
    @just frontend lint
    

all-clean:
    @just backend clean
    @just cli clean
    @just frontend clean
    
all-generate-openapi-client:
    @just cli generate-openapi-client
    @just frontend generate-openapi-client
    