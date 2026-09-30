# Proxy Formatter & Tester

## Overview

**Proxy Formatter & Tester** is a Python-based utility for preparing
proxy lists and checking whether the formatted proxies can successfully
connect to a user-provided test URL.

The project has two main processing stages:

1.  **Proxy Formatting** --- reads proxies in different input formats
    and converts valid entries into the standard
    `USERNAME:PASSWORD@HOST:PORT` format.
2.  **Proxy Testing** --- reads the formatted proxies and tests them
    against a URL using `curl_cffi`, while recording working and failed
    proxies separately.

The project is intended as a practical application of Python
programming, file handling, input validation, error handling, modular
programming, and external-library usage.

## Features

### 1. Proxy Formatting

The formatter currently supports:

-   `HOST:PORT:USERNAME:PASSWORD`
-   `USERNAME:PASSWORD@HOST:PORT`
-   Proxy strings with `http://`, `https://`, or `socks5://` prefixes
-   Labeled proxy fields such as:
    -   `IP: ...`
    -   `HOST: ...`
    -   `PORT: ...`
    -   `USERNAME: ...`
    -   `PASSWORD: ...`
-   Four consecutive unlabeled lines representing:
    -   HOST
    -   PORT
    -   USERNAME
    -   PASSWORD
-   URL-decoding of username/password fields
-   Port validation in the range `1–65535`
-   Duplicate removal while preserving input order
-   Invalid/unrecognized entry counting

The formatter writes the resulting proxies to `proxies.txt`.

### 2. Proxy Testing

The tester:

-   Reads proxies from `proxies.txt`
-   Accepts a test URL from the user
-   Adds an HTTP scheme when one is not supplied
-   Tests HTTP and HTTPS requests through each proxy
-   Uses `curl_cffi`
-   Uses Chrome impersonation for the request
-   Measures request time
-   Records HTTP status codes
-   Classifies common failures such as timeout, proxy connection
    failure, SSL failure, and connection failure
-   Saves working proxies to `working.txt`
-   Saves failed proxies to `fail.txt`
-   Saves detailed test information to `proxy_results.txt`
-   Displays a final test summary

## Workflow

``` text
Raw Proxy List
      |
      v
Proxy Formatter
      |
      v
proxies.txt
      |
      v
Proxy Tester
      |
      +-------------------+
      |                   |
      v                   v
 working.txt          fail.txt
      |
      v
proxy_results.txt
```

## Input / Output

### Formatter

**Input:** `unformat_proxy.txt`

**Output:** `proxies.txt`

The formatter reads non-empty lines, attempts to recognize supported
proxy formats, validates required fields, removes duplicates, and writes
valid formatted proxies.

### Tester

**Input:** `proxies.txt` + user-provided test URL

**Outputs:**

-   `working.txt` --- proxies whose request returned a successful HTTP
    response
-   `fail.txt` --- proxies whose request failed
-   `proxy_results.txt` --- detailed results including timestamp, URL,
    status, timing, and error information

## Technologies Used

-   Python
-   `pathlib`
-   `urllib.parse`
-   `datetime`
-   `curl_cffi`
-   File I/O
-   Exception handling
-   Input validation
-   Git / GitHub

## Project Structure

A recommended repository structure is:

``` text
proxy-formatter-tester/
│
├── formatter.py
├── proxy_tester.py
├── unformat_proxy.txt
├── proxies.txt
├── working.txt
├── fail.txt
├── proxy_results.txt
│
├── tests/
│   ├── test_formatter.py
│   └── test_proxy_tester.py
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   └── diagrams/
│
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

Generated result files can instead be excluded from GitHub if they
contain real proxy credentials.

## Installation

### 1. Clone the repository

``` bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd proxy-formatter-tester
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Create a `requirements.txt` containing:

``` text
curl_cffi
```

Then run:

``` bash
python -m pip install -r requirements.txt
```

## Usage

### Step 1 --- Prepare the input

Put the raw proxy list in:

``` text
unformat_proxy.txt
```

### Step 2 --- Format the proxies

Run:

``` bash
python formatter.py
```

The valid proxies will be written to:

``` text
proxies.txt
```

### Step 3 --- Test the proxies

Run:

``` bash
python proxy_tester.py
```

Enter the URL against which you want to test the proxies.

The tester will produce:

``` text
working.txt
fail.txt
proxy_results.txt
```

## Testing

The project should include validation tests for at least:

### Formatter tests

-   Valid `HOST:PORT:USERNAME:PASSWORD`
-   Valid `USERNAME:PASSWORD@HOST:PORT`
-   Valid labeled input
-   Invalid port
-   Missing username/password
-   Empty lines
-   Duplicate proxies
-   Unsupported formats

### Proxy tester tests

-   Valid proxy formatting
-   Missing HTTP scheme
-   Invalid/empty proxy
-   Successful response
-   Timeout
-   Connection failure
-   SSL-related failure
-   Correct writing to working/failed output files

Actual network proxy testing should be separated from automated unit
tests where possible.

## Error Handling

The formatter skips unrecognized entries and reports how many entries
were skipped.

The tester handles request exceptions and converts common errors into
readable categories, including:

-   Request timed out
-   Proxy connection failed
-   SSL verification failed
-   Connection failed

Unexpected exceptions are also captured and reported.

## Security and Privacy

Proxy credentials are sensitive information. Do not commit real proxy
usernames, passwords, or private proxy lists to a public GitHub
repository.

Use a `.gitignore` file to prevent accidental commits of
sensitive/generated files.

Example:

``` text
.venv/
__pycache__/
*.pyc

unformat_proxy.txt
proxies.txt
working.txt
fail.txt
proxy_results.txt
```

## Current Limitations

-   The tester currently focuses on HTTP/HTTPS proxy configuration.
-   Proxy protocol handling is not yet fully separated into
    protocol-specific testing.
-   The project currently uses a sequential testing workflow.
-   There is no automated test suite yet.
-   Configuration values such as timeout and impersonation are stored
    directly in the Python source.
-   There is no dedicated command-line argument interface yet.
-   Architecture/UML documentation still needs to be added for the
    academic submission.

## Future Enhancements

Possible future improvements include:

-   Command-line arguments for input/output files and test URL
-   Configurable timeout
-   Configurable concurrency
-   Retry support
-   More detailed statistics
-   Export to CSV/JSON
-   Unit tests
-   Logging system
-   Cleaner package structure
-   Protocol-specific proxy support
-   Progress reporting
-   A simple GUI
-   Automated report generation

## Academic Project Alignment

The project demonstrates:

-   Problem identification
-   Input processing
-   Data validation
-   File handling
-   Modular functions
-   External library integration
-   Error handling
-   Result generation
-   Testing requirements
-   Version control through Git/GitHub

The project should also include the required design diagrams,
documentation, testing evidence, and project report described in the
VITyarthi project guidelines.

## License

Add a suitable license if the project is intended for public
distribution.
