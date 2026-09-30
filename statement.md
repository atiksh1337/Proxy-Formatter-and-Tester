# Project Statement

## Project Title

**Proxy Formatter & Tester**

## Problem Statement

Proxy lists are often provided in inconsistent formats, making them
inconvenient to process directly in applications that require a standard
proxy representation. In addition, a proxy list may contain invalid,
unreachable, or non-responsive proxies.

The project addresses this problem by providing a Python-based workflow
that first converts supported proxy input formats into a consistent
`USERNAME:PASSWORD@HOST:PORT` representation and then tests the
formatted proxies against a user-selected URL.

The system separates valid formatted proxies from invalid/unresponsive
proxies and generates detailed test results for further analysis.

## Scope of the Project

The project covers two primary stages:

1.  **Proxy formatting**
    -   Read proxy information from a text file.
    -   Recognize supported proxy formats.
    -   Validate required fields and port numbers.
    -   Convert valid entries to a standard format.
    -   Remove duplicate formatted proxies.
    -   Save the resulting list to `proxies.txt`.
2.  **Proxy testing**
    -   Read formatted proxies from `proxies.txt`.
    -   Accept a test URL from the user.
    -   Send requests through each proxy.
    -   Measure request time and record HTTP status.
    -   Classify common request failures.
    -   Save successful proxies to `working.txt`.
    -   Save failed proxies to `fail.txt`.
    -   Store detailed results in `proxy_results.txt`.

The project does not aim to provide a proxy provider, anonymous browsing
service, or proxy acquisition system. Its scope is limited to processing
and testing proxy data supplied by the user.

## Target Users

The intended users are:

-   Students learning Python programming and file processing.
-   Developers who need to normalize proxy-list data.
-   Users who need a basic utility for validating supplied proxy lists.
-   Students demonstrating practical applications of programming
    concepts in an academic project.

## High-Level Features

### Proxy Formatting

-   Multiple input-format recognition
-   Username/password extraction
-   Host and port extraction
-   Port validation
-   Labeled-field parsing
-   Duplicate removal
-   Invalid-entry handling
-   Formatted output generation

### Proxy Testing

-   User-provided test URL
-   Proxy-based HTTP/HTTPS requests
-   Request timing
-   HTTP status recording
-   Error classification
-   Working/failed proxy separation
-   Detailed result logging

## Functional Requirements

### FR1 --- Read Proxy Input

The system shall read proxy entries from an input text file.

### FR2 --- Recognize Supported Formats

The system shall recognize supported proxy representations, including
direct proxy URLs, `HOST:PORT:USERNAME:PASSWORD`, labeled fields, and
four-line raw entries.

### FR3 --- Validate Proxy Data

The system shall validate the presence of required fields and ensure
that ports are numeric and within the valid range of `1–65535`.

### FR4 --- Generate Standard Proxy Format

The system shall convert valid entries into:

``` text
USERNAME:PASSWORD@HOST:PORT
```

### FR5 --- Remove Duplicates

The formatter shall remove duplicate formatted proxy entries while
preserving their order.

### FR6 --- Test Proxies

The tester shall send requests through each formatted proxy to a
user-provided test URL.

### FR7 --- Record Test Results

The tester shall record success status, HTTP status where available,
request time, and error information.

### FR8 --- Separate Results

The tester shall save working and failed proxies into separate output
files.

## Non-Functional Requirements

### NFR1 --- Performance

The system should process proxy entries without unnecessary repeated
parsing and should provide request timing information during testing.

### NFR2 --- Reliability

Invalid proxy entries and request failures should not terminate the
complete processing workflow.

### NFR3 --- Usability

The programs should provide clear terminal messages describing input
requirements, progress, errors, and final results.

### NFR4 --- Maintainability

The implementation should use separate functions for formatting,
validation, error classification, proxy testing, and program control.

### NFR5 --- Error Handling

The system should handle invalid input files, malformed proxy entries,
request exceptions, timeouts, and other runtime errors gracefully.

### NFR6 --- Resource Efficiency

Input and output files should be processed using normal file-handling
practices without unnecessarily loading large amounts of repeated data
into memory.

## Expected Workflow

``` text
User
 |
 | Provides raw proxy list
 v
Formatter
 |
 | Validate + normalize
 v
proxies.txt
 |
 | User provides test URL
 v
Proxy Tester
 |
 +----------------------+
 |                      |
 v                      v
Working Proxies     Failed Proxies
 |                      |
 v                      v
working.txt          fail.txt
          \          /
           \        /
            v      v
        proxy_results.txt
```

## Expected Project Outcome

At the end of execution, the user should have:

-   A normalized proxy list.
-   A list of proxies that successfully completed the test request.
-   A list of proxies that failed the test.
-   A detailed record of the testing process.
-   A reusable Python-based workflow for proxy-list processing.

## Out of Scope

The following are outside the scope of this project:

-   Obtaining or purchasing proxies.
-   Generating proxy credentials.
-   Bypassing authentication or access controls.
-   Circumventing website security mechanisms.
-   Providing anonymity guarantees.
-   Determining whether a proxy is suitable for a particular service
    beyond the supplied connectivity test.

## Academic Relevance

The project applies programming concepts through a practical problem
involving:

-   Functions
-   Conditional statements
-   Loops
-   Strings and parsing
-   Lists and dictionaries
-   File handling
-   Exception handling
-   External libraries
-   Input validation
-   Modular programming
-   Basic testing and result analysis
