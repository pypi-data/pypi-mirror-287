import asyncio
from typing import Any

from harambe import SDK, Schemas
from harambe.contrib import playwright_harness


async def scrape(
    sdk: SDK, url: str, context: Any, *args: Any, **kwargs: Any
) -> None:
    page = sdk.page
    await page.type("#username", "hazel20240116@gmail.com", delay=75)
    await page.type("#password", "SV7Gp#V#sXg2We3", delay=75)
    await asyncio.sleep(1)
    await page.click('input[type="submit"]')

    await asyncio.sleep(3)
    await page.goto(
        "https://www.bidsync.com/bidsync-app-web/vendor/links/BidDetail.xhtml?bidid=2128512"
    )
    await asyncio.sleep(3)
    all_cookies = await page.context.cookies()

    new_cookies = [
        Cookie(**cookie)
        for cookie in all_cookies
        if cookie["name"] in ["JSESSIONID", "AWSALB", "AWSALBCORS"]
    ]
    return new_cookies




if __name__ == "__main__":
    asyncio.run(SDK.run(scrape, 'https://www.bidsync.com/bidsync-cas/', schema=Schemas.government_contracts, harness=playwright_harness, headless=False, stealth=False))
