---
layout: post
title:  "Implied Volatilities - Crypto Options"
categories: fx, crypto
---

Noted: 
* This is incomplete.
* Todos: handle extrapolations. clean up notebook. create an iv matrix. 


[Deribit](https://www.deribit.com/) provides public APIs to request market data of options on crypto currencies including BTC and ETH. Since cryptos are currencies,
let's look for risk reversals and butterflies. Nothing new other than applying standards from the FX market and doing my own revisions on the subject ([jupyter notebook](https://github.com/xyise/xyise/tree/main/notebook/deribit) - needs clean-up).



To this end, 
* Download option market data from Deribit. Greeks including deltas are already included in the data. 
* Interpolate implied volatilities for 10P, 25P, ATM, 25C, 10C.
* Set ATM, 25RR, 25FLY, 10RR, 10FLY


![plot](/assets/crypto-rr-fly/rr-st.png)
