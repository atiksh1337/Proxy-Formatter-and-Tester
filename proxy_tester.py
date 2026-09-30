import time
from datetime import datetime
from curl_cffi import requests as cf_requests
from curl_cffi.requests.exceptions import RequestException
from config import FORMATTED_FILE, RESULT_FILE, WORKING_FILE, FAILED_FILE, TIMEOUT, IMPERSONATE
from error_handler import classify_error


def format_proxy(proxy):
    proxy = proxy.strip()
    if not proxy:
        return None
    if not proxy.startswith(("http://", "https://")):
        proxy = "http://" + proxy
    return proxy


def test_proxy(proxy, test_url):
    proxy_url = format_proxy(proxy)
    if not proxy_url:
        return None
    proxies = {"http": proxy_url, "https": proxy_url}
    start = time.time()
    try:
        response = cf_requests.get(test_url, proxies=proxies, timeout=TIMEOUT, impersonate=IMPERSONATE)
        elapsed = round(time.time() - start, 2)
        return {"proxy": proxy.strip(), "status": response.status_code, "time": elapsed,
                "success": response.ok, "error": None}
    except RequestException as exc:
        elapsed = round(time.time() - start, 2)
        return {"proxy": proxy.strip(), "status": None, "time": elapsed,
                "success": False, "error": classify_error(exc)}
    except Exception as exc:
        elapsed = round(time.time() - start, 2)
        return {"proxy": proxy.strip(), "status": None, "time": elapsed,
                "success": False, "error": str(exc)}


def run_tests(test_url, proxy_file=FORMATTED_FILE):
    with open(proxy_file, "r", encoding="utf-8") as file:
        proxies = [line.strip() for line in file if line.strip()]
    working = failed = 0
    with open(RESULT_FILE, "w", encoding="utf-8") as output, \
         open(WORKING_FILE, "w", encoding="utf-8") as working_file, \
         open(FAILED_FILE, "w", encoding="utf-8") as failed_file:
        output.write(f"Proxy Test Results - {datetime.now()}\n")
        output.write(f"Test URL: {test_url}\n")
        output.write(f"Impersonate: {IMPERSONATE}\n")
        output.write("=" * 70 + "\n\n")
        for index, proxy in enumerate(proxies, 1):
            print(f"[{index}/{len(proxies)}] Testing proxy...")
            result = test_proxy(proxy, test_url)
            if result is None:
                continue
            if result["success"]:
                working += 1; working_file.write(result["proxy"] + "\n")
                message = f"[WORKING] {result['proxy']} | Status: {result['status']} | Time: {result['time']}s"
            else:
                failed += 1; failed_file.write(result["proxy"] + "\n")
                message = f"[FAILED] {result['proxy']} | Error: {result['error']}"
                if result["status"] is not None:
                    message += f" | Status: {result['status']}"
            print(message); output.write(message + "\n")
    print("\n" + "=" * 55)
    print("                  TEST SUMMARY")
    print("=" * 55)
    print(f"Total proxies : {len(proxies)}")
    print(f"Working       : {working}")
    print(f"Failed        : {failed}")
    print(f"\nDetailed results saved to {RESULT_FILE}")
    print(f"Working proxies saved to {WORKING_FILE}")
    print(f"Failed proxies saved to {FAILED_FILE}")
    return len(proxies), working, failed


def main():
    print("=" * 55)
    print("        CURL_CFFI-BASED PROXY TESTER")
    print("=" * 55)
    test_url = input("\nEnter test URL (e.g. https://example.com): ").strip()
    if not test_url.startswith(("http://", "https://")):
        test_url = "https://" + test_url
    try:
        run_tests(test_url)
    except FileNotFoundError:
        print(f"\nError: {FORMATTED_FILE} was not found.")


if __name__ == "__main__":
    main()
