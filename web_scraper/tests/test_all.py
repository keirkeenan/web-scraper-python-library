# disable the following pylint warnings:
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=wrong-import-position

import unittest
from unittest.mock import patch
from web_scraper.main import get_html, parse_itemprice, scrape_ebay, scrape_walmart, scrape_amazon, scrape, scrape_all


class TestMethods(unittest.TestCase):
    # Test the get_html function

    def test_ebay(self):
        # Test with valid input
        html = get_html("ebay", "pencil", 1)
        self.assertTrue("<!DOCTYPE html>" in html)

    # def test_walmart(self):
    #     # Test with valid input
    #     html = get_html("walmart", "pencil", 1)
    #     self.assertTrue("<!DOCTYPE html>" in html)

    def test_amazon(self):
        # Test with valid input
        html = get_html("amazon", "pencil", 1)
        self.assertTrue("<!doctype html>" in html)

    def test_wrong_company_name(self):
        # Test with invalid input
        html = get_html("wrong", "pencil", 1)
        self.assertEqual(html, "Something went wrong. Please try again.")

    # ===================================#

    # Test the parse_itemprice function

    def test_parse_itemprice_valid(self):
        # Test with valid input
        result = parse_itemprice("$123.45")
        expected_output = 123.45
        self.assertEqual(result, expected_output)

    # ===================================#

    # Test the scrape functions

    def test_scrape_ebay_valid(self):
        # Test with valid input
        result = scrape_ebay("pencil")
        not_expected_output = "Failed to collect data from eBay. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)

    def test_scrape_walmart_mock(self):
        # Set up mock response for get_html
        mock_html = '<!DOCTYPE html><body><div class="mb0 ph1 pa0-xl bb b--near-white w-25"><div style="contain-intrinsic-size:198px 340px" class="h-100 pb1-xl pr4-xl pv3 ph1"><div data-item-id="1ZH03JCE3JSS" class="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity"><a link-identifier="14977443" href="https://wrd.walmart.com/track?adUid=4c7a1615-1b6c-4743-a0ed-a18fcbd6bf6b&amp;pgId=pencil&amp;spQs=t8GXwbg0EFm3fn92HprVu77SJYyqzBpnp0an539TanzxdqlqncZUo3saIZZU1jMbu79F6El8NbCEG68wk4Nku1ETMd73EoAVCqjR-ce-MXNbODLGAi_LKmNvHR1khRCvjb3pDTDSIJNvqFpKkgGWMU2oy69l3DtcGtbDnLCnIZ_0H1eELCYiv5Mxz-lgO0O5i2PwnwAV0VyHD3AlOIF-F3ZhzAGPlO-8kIHU13-3ejo&amp;storeId=3520&amp;pt=search&amp;mloc=sp-search-middle&amp;bkt=2654&amp;pltfm=desktop&amp;rdf=1&amp;plmt=sp-search-middle~desktop~&amp;eventST=click&amp;pos=2&amp;bt=1&amp;tax=1229749_1431586_6267234_1778429&amp;et=head_torso&amp;st=torso&amp;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FBIC-Xtra-Strong-Thick-Lead-Mechanical-Pencil-Black-Thick-Point-0-9mm-24-Count%2F14977443%3Fathbdg%3DL1600%26adsRedirect%3Dtrue&amp;couponState=na&amp;athbdg=L1600" class="absolute w-100 h-100 z-1 hide-sibling-opacity" target=""><span class="w_iUH7">BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count<!-- --> </span></a><div class="" data-testid="list-view"><div class=""><div class="h2 relative mb2"><span class="w_VbBP w_mFV6 w_awtt w_3oNC w_3H8O absolute tag-leading-badge">Best seller</span></div><div class="relative"><div class="relative overflow-hidden" style="max-width:290px;height:0;padding-bottom:min(392px, 135.17241379310346%);align-self:center;width:min(290px, 100%)"><img loading="eager" width="" height="" class="absolute top-0 left-0" data-testid="productTileImage" alt="BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count" src="https://i5.walmartimages.com/asr/7691c1c3-3b23-418b-9591-2bd707d211b3.43afcf901046d245d286f2b94f582190.png?odnHeight=784&amp;odnWidth=580&amp;odnBg=FFFFFF"/></div><div class="z-2 absolute bottom--1"><div class="relative dib"><a class="w_hhLG w_8nsR w_jDfj pointer bn sans-serif b ph2 flex items-center justify-center w-auto shadow-1" href="https://wrd.walmart.com/track?adUid=4c7a1615-1b6c-4743-a0ed-a18fcbd6bf6b&amp;pgId=pencil&amp;spQs=t8GXwbg0EFm3fn92HprVu77SJYyqzBpnp0an539TanzxdqlqncZUo3saIZZU1jMbu79F6El8NbCEG68wk4Nku1ETMd73EoAVCqjR-ce-MXNbODLGAi_LKmNvHR1khRCvjb3pDTDSIJNvqFpKkgGWMU2oy69l3DtcGtbDnLCnIZ_0H1eELCYiv5Mxz-lgO0O5i2PwnwAV0VyHD3AlOIF-F3ZhzAGPlO-8kIHU13-3ejo&amp;storeId=3520&amp;pt=search&amp;mloc=sp-search-middle&amp;bkt=2654&amp;pltfm=desktop&amp;rdf=1&amp;plmt=sp-search-middle~desktop~&amp;eventST=click&amp;pos=2&amp;bt=1&amp;tax=1229749_1431586_6267234_1778429&amp;et=head_torso&amp;st=torso&amp;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FBIC-Xtra-Strong-Thick-Lead-Mechanical-Pencil-Black-Thick-Point-0-9mm-24-Count%2F14977443%3Fathbdg%3DL1600%26adsRedirect%3Dtrue&amp;couponState=na&amp;athbdg=L1600" aria-label="Options - BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count"><span class="mh2">Options</span></a></div></div></div><div class="mt5 mb0" style="height:24px" data-testid="variant-1ZH03JCE3JSS"><div class="flex items-center lh-title h2-l normal"><span class="gray f7">Sponsored</span></div></div></div><div class=""><div data-automation-id="product-price" class="flex flex-wrap justify-start items-center lh-title mb1"><div class="mr1 mr2-xl b black green lh-copy f5 f4-l" aria-hidden="true">Now $6.22</div><span class="w_iUH7">current price Now $6.22</span><div class="gray mr1 strike f7 f6-l" aria-hidden="true">$11.26</div><span class="w_iUH7">Was $11.26</span><div class="f7 f6-l gray mr1">$6.22/ea</div></div><span class="w_V_DM" style="-webkit-line-clamp:3;padding-bottom:0em;margin-bottom:-0em"><span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count</span></span><div class="flex items-center mt2"><span class="black inline-flex mr1"><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarHalf" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i></span><span class="sans-serif gray f7" aria-hidden="true">147</span><span class="w_iUH7">4.7 out of 5 Stars. 147 reviews</span></div><div></div><div class="flex items-center mv2"><div class="f7 mr1 blue b lh-copy">Save with</div><img loading="lazy" class="flex" src="//i5.walmartimages.com/dfw/63fd9f59-ac39/29c6759d-7f14-49fa-bd3a-b870eb4fb8fb/v1/wplus-icon-blue.svg" alt="Walmart Plus" height="20" width="20"/></div><div class="mt2 mb2"><span class="w_VbBP w_mFV6 w_I_19 w_3oNC w_AAn7 mr1 mt1 ph1">Pickup</span><span class="w_VbBP w_mFV6 w_I_19 w_3oNC w_AAn7 mr1 mt1 ph1">2-day shipping</span></div></div></div></div></div></div></body></html>'
        with patch("web_scraper.main.get_html", return_value=mock_html):
            # Test with valid input
            result = scrape_walmart("pencil")
            not_expected_output = "Failed to collect data from Walmart. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
            self.assertNotEqual(result, not_expected_output)

    def test_scrape_amazon_valid(self):
        # Set up mock response for get_html
        mock_html = '<!doctype html><body><div data-component-type="s-impression-counter" data-component-props="{&#34;presenceCounterName&#34;:&#34;sp_delivered&#34;,&#34;testElementSelector&#34;:&#34;.s-image&#34;,&#34;hiddenCounterName&#34;:&#34;sp_hidden&#34;}" class="rush-component s-featured-result-item s-expand-height"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t1 puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section a-spacing-base"><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized"><span data-component-type="s-product-image" class="rush-component"><a class="a-link-normal s-no-outline" href="/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_next_aps_sr_pg3_1?ie=UTF8&amp;adId=A03308292GSQXN8CYOUFH&amp;qualifier=1680823514&amp;id=4536982638462727&amp;widgetName=sp_atf_next&amp;url=%2FBIC-Xtra-Life-Mechanical-Pencil-40-Count%2Fdp%2FB01JHMVG5O%2Fref%3Dsr_1_97_sspa%3Fkeywords%3Dpencil%26qid%3D1680823514%26sr%3D8-97-spons%26psc%3D1"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL320_.jpg" srcset="https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL320_.jpg 1x, https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL480_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL640_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL800_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81QprHooW-L._AC_UL960_FMwebp_QL65_.jpg 3x" alt="Sponsored Ad - BIC Xtra-Smooth Mechanical Pencil, Medium Point (0.7mm), Perfect For The Classroom &amp; Test Time, 40-Count" data-image-index="97" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"/></div></a></span></div><div class="a-section a-spacing-small puis-padding-left-small puis-padding-right-small"><div class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"><div class="a-row a-spacing-micro"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:&quot;true&quot;,&quot;dataStrategy&quot;:&quot;preload&quot;,&quot;name&quot;:&quot;sp-info-popover-B01JHMVG5O&quot;,&quot;position&quot;:&quot;triggerVertical&quot;}"><a href="javascript:void(0)" role="button" style="text-decoration: none;" aria-label="View Sponsored information or leave ad feedback" class="puis-label-popover puis-sponsored-label-text"><span class="puis-label-popover-default"><span class="a-color-secondary">Sponsored</span></span><span class="puis-label-popover-hover"><span class="a-color-base">Sponsored</span></span> <span class="aok-inline-block puis-sponsored-label-info-icon"></span></a></span><div class="a-popover-preload" id="a-popover-sp-info-popover-B01JHMVG5O"><div class="puis"><span>You’re seeing this ad based on the product’s relevance to your search query.</span><div class="a-row"><span class="a-declarative" data-action="s-safe-ajax-modal-trigger" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-safe-ajax-modal-trigger" data-s-safe-ajax-modal-trigger="{&quot;ajaxUrl&quot;:&quot;/af/sp-loom/feedback-form?pl=%7B%22adPlacementMetaData%22%3A%7B%22searchTerms%22%3A%22cGVuY2ls%22%2C%22pageType%22%3A%22Search%22%2C%22feedbackType%22%3A%22sponsoredProductsLoom%22%2C%22slotName%22%3A%22TOP%22%7D%2C%22adCreativeMetaData%22%3A%7B%22adProgramId%22%3A1024%2C%22adCreativeDetails%22%3A%5B%7B%22asin%22%3A%22B01JHMVG5O%22%2C%22title%22%3A%22BIC+Xtra-Smooth+Mechanical+Pencil%2C+Medium+Point+%280.7mm%29%2C+Perfect+For+The+Classroom+%26+Test+Time%2C+40-C%22%2C%22priceInfo%22%3A%7B%22amount%22%3A10.37%2C%22currencyCode%22%3A%22USD%22%7D%2C%22sku%22%3A%22B01JHMVG5O%22%2C%22adId%22%3A%22A03308292GSQXN8CYOUFH%22%2C%22campaignId%22%3A%22A03945172W7CX3FZRI6LE%22%2C%22advertiserIdNS%22%3Anull%2C%22selectionSignals%22%3Anull%7D%5D%7D%7D&quot;,&quot;dataStrategy&quot;:&quot;ajax&quot;,&quot;header&quot;:&quot;Share your feedback&quot;}"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="#"><span>Leave ad feedback</span> </a> </span></div></div></div></div><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_next_aps_sr_pg3_1?ie=UTF8&amp;adId=A03308292GSQXN8CYOUFH&amp;qualifier=1680823514&amp;id=4536982638462727&amp;widgetName=sp_atf_next&amp;url=%2FBIC-Xtra-Life-Mechanical-Pencil-40-Count%2Fdp%2FB01JHMVG5O%2Fref%3Dsr_1_97_sspa%3Fkeywords%3Dpencil%26qid%3D1680823514%26sr%3D8-97-spons%26psc%3D1"><span class="a-size-base-plus a-color-base a-text-normal">BIC Xtra-Smooth Mechanical Pencil, Medium Point (0.7mm), Perfect For The Classroom &amp; Test Time, 40-Count</span> </a> </h2></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.8 out of 5 stars"><span class="a-size-base">4.8</span><span class="a-letter-space"></span><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B01JHMVG5O&amp;ref=acr_search__popover&amp;contextId=search&quot;}"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-5 aok-align-bottom"><span class="a-icon-alt">4.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="45,440"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_next_aps_sr_pg3_1?ie=UTF8&amp;adId=A03308292GSQXN8CYOUFH&amp;qualifier=1680823514&amp;id=4536982638462727&amp;widgetName=sp_atf_next&amp;url=%2FBIC-Xtra-Life-Mechanical-Pencil-40-Count%2Fdp%2FB01JHMVG5O%2Fref%3Dsr_1_97_sspa%3Fkeywords%3Dpencil%26qid%3D1680823514%26sr%3D8-97-spons%26psc%3D1#customerReviews"><span class="a-size-base s-underline-text">(45,440)</span> </a> </span></div><div class="a-row a-size-base"><span class="a-size-base a-color-secondary">1K+ bought in past week</span></div></div><div class="a-section a-spacing-none a-spacing-top-small s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_next_aps_sr_pg3_1?ie=UTF8&amp;adId=A03308292GSQXN8CYOUFH&amp;qualifier=1680823514&amp;id=4536982638462727&amp;widgetName=sp_atf_next&amp;url=%2FBIC-Xtra-Life-Mechanical-Pencil-40-Count%2Fdp%2FB01JHMVG5O%2Fref%3Dsr_1_97_sspa%3Fkeywords%3Dpencil%26qid%3D1680823514%26sr%3D8-97-spons%26psc%3D1"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$10.37</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">10<span class="a-price-decimal">.</span></span><span class="a-price-fraction">37</span></span></span> <span class="a-size-base a-color-secondary">($0.26/Count)</span> <div style="display: inline-block"><span class="a-size-base a-color-secondary">List: </span><span class="a-price a-text-price" data-a-size="b" data-a-strike="true" data-a-color="secondary"><span class="a-offscreen">$13.99</span><span aria-hidden="true">$13.99</span></span></div> </a> </div><div class="a-row a-size-base a-color-secondary"><span>Save more with Subscribe &amp; Save</span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><div class="a-row s-align-children-center"><span class="aok-inline-block s-image-logo-view"><span class="aok-relative s-icon-text-medium s-prime"><i class="a-icon a-icon-prime a-icon-medium" role="img" aria-label="Amazon Prime"></i></span><span></span></span> </div><div class="a-row"><span aria-label="FREE delivery Wed, Apr 12 on $25 of items shipped by Amazon"><span class="a-color-base">FREE delivery </span><span class="a-color-base a-text-bold">Wed, Apr 12 </span><span class="a-color-base">on $25 of items shipped by Amazon</span><br/></span></div><div class="a-row"><span aria-label="Or fastest delivery Sat, Apr 8 "><span class="a-color-base">Or fastest delivery </span><span class="a-color-base a-text-bold">Sat, Apr 8 </span></span></div></div></div></div></div></div></div></body></html>'
        with patch("web_scraper.main.get_html", return_value=mock_html):
            # Test with valid input
            result = scrape_amazon("pencil")
            not_expected_output = "Failed to collect data from Amazon. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
            self.assertNotEqual(result, not_expected_output)

    # ===================================#

    # Test the main function

    def test_main_valid(self):
        # Test with valid input
        result = scrape("pencil", "ebay")
        not_expected_output = "Failed to collect data from eBay."
        self.assertNotEqual(result, not_expected_output)

    def test_main_invalid(self):
        # Test with invalid input
        result = scrape("pencil", "Random Company")
        expected_output = "Scraper not available for `Random Company`. Try: eBay, Walmart, or Amazon."
        self.assertEqual(result, expected_output)

    # ===================================#

    # Test the scrape_all function

    def test_scrape_all_success(self):
        # Test with valid input
        result = scrape_all("pencil")
        not_expected_output = "Failed to collect any data. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)


if __name__ == "__main__":
    unittest.main()
