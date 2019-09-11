# Error-Correcting-Code
* Hamming codes have one issue: they can only encode messages of length k, where k = 2r − r − 1 for some r ≥ 2. The algorithmconverts any vector into an encodable message. This is done as follows. Let a be a vector of length l ≥ 1. Choose r ≥ 2 so that k−r = 2r −2r−1 ≥ l
and is as small as possible, then let m = (m1, . . . , mk) such that:

  * (m1, . . . , mr) represents l in binary,
  * (mr+1, . . . , mr+l) = a,
  * (mr+l+1, . . . , mk) = (0, . . . , 0)

