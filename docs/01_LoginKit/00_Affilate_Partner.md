# Get affiliate list
----------
Get list of affiliate partner. In case success, it will return a list of Affiliate Partner.
```java
LoginKit.getInstance().getAffiliates(affiliateList -> {
    Log.d("AffiliateList", affiliateList);
}, Throwable::printStackTrace);
```
```swift
LoginKit.mainInstance().getAffiliates({
    partnerList in print(partnerList?.affiliates)
    }, failureBlock: {
        error in print(error?.message)
})
```
# Using OAuthWebView
----------
Set up partner WebView to get auth token for register account.
```java
// Put OAuthWebView into your layout
void affiliatePartnerSignIn(OAuthWebView oauthWebView, Affiliate affiliate) {
    oAuthWebView.loadAuthorizeUrl(affiliate.getUrl(), token -> {
        Log.d("Auth token", token);
    })
}
```
```swift
let oAuthWebView = OAuthLoginKitView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
oAuthWebView.providerID = your_partner_affiate_id
oAuthWebView._delegate = self
view.addSubview(oAuthWebView)
```
# Sign up account for affiliate partner
-------
```java
LoginKit.getInstance().affiliateSignUp("TestName", "testKaiwei@gmail.com", "12345678", token,
                                        accountInfo -> {
                                            Log.d("Token", accountInfo.token);
                                            Log.d("RefreshToken", accountInfo.refreshToken);
                                        }, Throwable::printStackTrace)
```
```swift
LoginKit.loginInstance.signUpAffiliateAccount("TestName", email: "testKaiwei@gmail.com", password: "12345678", registerToken: token, successBlock: { model in
            print(model!.authToken)
            print(model!.registerToken)
        }, failureBlock: { error in
            print(error!.message)
    })
```
