OPENRANGE = {"9":{"open":{"aggressive":{}, "normal":{}, "passive":{}}}, "6":{"open":{"aggressive":{}, "normal":{}, "passive":{}}}}

OPENRANGE['9']['open']['aggressive'].update({   "UTG":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+", 
                                                "UTG+1":    "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+", 
                                                "MP":       "22+, ATs+, KQs, QJs, JTs, T9s, 98s, AJo+",
                                                "MP+1":     "22+, ATs+, KQs, QJs, JTs, T9s, 98s, 87s, 76s, ATo+, KQo",
                                                "HJ":       "22+, A9s+, KJs+, QTs+, J9s+, T8s+, 97s+, 87s, 76s, 65s, ATo+, KQo",
                                                "CO":       "22+, A2s+, K9s+, Q9s+, J8s+, T8s+, 97s+, 86s+, 75s+, 64s+, 54s, A2o+, KTo+, QTo+, J9o+, T8o+, 98o, 87o, 76o",
                                                "BU":       "22+, A2s+, K2s+, Q4s+, J7s+, T8s+, 97s+, 86s+, 75s+, 64s+, 54s, A2o+, K7o+, Q8o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o",
                                                "SB":       "22+, A2s+, K9s+, Q9s+, J9s+, T8s+, 97s+, 86s+, 76s, 65s, 54s, ATo+, KTo+, QTo+, J9o+, T8o+, 98o",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })

OPENRANGE['9']['open']['normal'].update({       "UTG":      "77+, AQs+, AKo", 
                                                "UTG+1":    "77+, AQs+, AKo", 
                                                "MP":       "77+, AQs+, AQo+",
                                                "MP+1":     "66+, AJs+, KQs, QJs, JTs, T9s, 98s, 87s, AJo+, KQo",
                                                "HJ":       "55+, ATs+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, ATo+, KQo",
                                                "CO":       "22+, A7s+, K9s+, Q9s+, J9s+, T8s+, 97s+, 87s, 76s, 65s, 54s, A9o+, KTo+, QTo+, JTo, T9o, 98o, 87o",
                                                "BU":       "22+, A2s+, K9s+, Q9s+, J8s+, T8s+, 97s+, 86s+, 75s+, 65s, 54s, A2o+, KTo+, QTo+, J9o+, T8o+, 98o, 87o, 76o, 65o",
                                                "SB":       "22+, A2s+, K9s+, Q9s+, J9s+, T9s, 98s, 87s, 76s, 65s, 54s, ATo+, KTo+, QTo+, JTo",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })

OPENRANGE['9']['open']['passive'].update({      "UTG":      "TT+, AQs+, AKo", 
                                                "UTG+1":    "TT+, AQs+, AKo", 
                                                "MP":       "TT+, AQs+, AKo",
                                                "MP+1":     "99+, AJs+, AQo+",
                                                "HJ":       "88+, AJs+, KQs, AJo+, KQo",
                                                "CO":       "22+, A9s+, KTs+, QTs+, JTs, T9s, 98s, 87s, ATo+, KTo+, QTo+, JTo",
                                                "BU":       "22+, A2s+, K9s+, Q9s+, J8s+, T9s, 98s, 87s, 76s, 65s, 54s, A8o+, KTo+, QTo+, JTo, T9o, 98o",
                                                "SB":       "77+, A7s+, K9s+, Q9s+, J9s+, T9s, 98s, 87s, ATo+, KTo+, QTo+, JTo",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })

OPENRANGE['6']['open']['aggressive'].update({   "UTG":      "22+, ATs+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, ATo+, KJo+",                                                 
                                                "MP":       "22+, A9s+, KJs+, QTs+, JTs, T9s, 98s, 87s, 76s, 65s, A9o+, KJo+, QJo", 
                                                "CO":       "22+, A2s+, K7s+, Q7s+, J7s+, T8s+, 97s+, 87s, 76s, 65s, 54s, A2o+, K8o+, Q8o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o", 
                                                "BU":       "22+, A2s+, K2s+, Q2s+, J5s+, T8s+, 97s+, 87s, 76s, 65s, 54s, A2o+, K2o+, Q8o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o", 
                                                "SB":       "22+, A2s+, K7s+, Q7s+, J7s+, T8s+, 97s+, 87s, 76s, 65s, 54s, A2o+, K8o+, Q8o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })

OPENRANGE['6']['open']['normal'].update({       "UTG":      "22+, ATs+, KQs, AJo+, KQo",                                                 
                                                "MP":       "22+, ATs+, KJs+, ATo+, KJo+", 
                                                "CO":       "22+, A6s+, K9s+, Q9s+, J9s+, T8s+, 98s, 87s, 76s, 65s, A9o+, K9o+, Q9o+, J9o+, T9o, 98o, 87o", 
                                                "BU":       "22+, A2s+, K7s+, Q7s+, J7s+, T8s+, 97s+, 87s, 76s, 65s, 54s, A2o+, K8o+, Q8o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o", 
                                                "SB":       "22+, A6s+, K9s+, Q9s+, J8s+, T9s, 98s, 87s, 76s, ATo+, K9o+, Q9o+, J9o+",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })

OPENRANGE['6']['open']['passive'].update({      "UTG":      "66+, AJs+, AQo+",                                                 
                                                "MP":       "66+, AJs+, KQs, AJo+, KQo", 
                                                "CO":       "22+, A7s+, K9s+, Q9s+, J9s+, T8s+, A9o+, K9o+, QTo+, J9o+", 
                                                "BU":       "22+, A2s+, K8s+, Q8s+, J7s+, T9s, 98s, 87s, 76s, 65s, 54s, A9o+, K9o+, Q9o+, J8o+, T8o+, 97o+, 87o, 76o, 65o, 54o", 
                                                "SB":       "22+, ATs+, KTs+, QTs+, JTs, ATo+, KTo+, QTo+, JTo",
                                                "BB":      "22+, AJs+, KQs, QJs, JTs, T9s, 98s, AQo+"
                                            })


BETvsPFR = {"9":{"aggressive":{}, "normal":{}, "passive":{}}, "6":{"aggressive":{}, "normal":{}, "passive":{}}}

BETvsPFR['9']['aggressive'].update({   "UTG":      "JJ+, AKs, AKo", 
                                        "UTG+1":    "JJ+, AKs, AKo",
                                        "MP":       "99+, AJs+, AQo+",
                                        "MP+1":     "88+, ATs+, KQs, ATo+, KQo",
                                        "HJ":       "88+, ATs+, KQs, ATo+, KQo",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })

BETvsPFR['9']['normal'].update({       "UTG":      "JJ+, AKs, AKo", 
                                        "UTG+1":    "JJ+, AKs, AKo",
                                        "MP":       "99+, AJs+, AQo+",
                                        "MP+1":     "88+, ATs+, KQs, ATo+, KQo",
                                        "HJ":       "88+, ATs+, KQs, ATo+, KQo",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })

BETvsPFR['9']['passive'].update({      "UTG":      "JJ+, AKs, AKo", 
                                        "UTG+1":    "JJ+, AKs, AKo",
                                        "MP":       "99+, AJs+, AQo+",
                                        "MP+1":     "88+, ATs+, KQs, ATo+, KQo",
                                        "HJ":       "88+, ATs+, KQs, ATo+, KQo",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })

BETvsPFR['6']['aggressive'].update({   "UTG":      "JJ+, AKs, AKo", 
                                        "MP":       "99+, AJs+, AQo+",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })

BETvsPFR['6']['normal'].update({       "UTG":      "JJ+, AKs, AKo", 
                                        "MP":       "99+, AJs+, AQo+",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })

BETvsPFR['6']['passive'].update({      "UTG":      "JJ+, AKs, AKo", 
                                        "MP":       "99+, AJs+, AQo+",
                                        "CO":       "33+, A2s+, KTs+, A8o+, KTo+",
                                        "BU":       "22+, A2s+, K8s+, QTs+, A2o+, K9o+",
                                        "SB":       "QQ+, AKs",
                                        "BB":       "QQ+, AKs"
                                    })




CALLING = {     "9":{"UTG":{}, "UTG+1":{}, "MP":{}, "MP+1":{}, "HJ":{}, "CO":{}, "BU":{},"SB":{}, "BB":{}},  
                "6":{"UTG":{}, "MP":{}, "CO":{}, "BU":{},"SB":{}, "BB":{}}}

CALLING['9']['UTG'].update({    "UTG":      "NONE", 
                                "UTG+1":    "QQ+, AKs, AKo", 
                                "MP":       "QQ+, AJs+, KQs, AQo+", 
                                "MP+1":     "QQ+, AJs+, KQs, AQo+", 
                                "HJ":       "QQ+, AJs+, KQs, AQo+", 
                                "CO":       "QQ+, AJs+, KQs, AQo+", 
                                "BU":       "QQ+, AJs+, KQs, AQo+", 
                                "SB":       "JJ+, AQs+, KQs, AKo",
                                "BB":       "JJ+, AQs+, KQs, AKo"
                            })
CALLING['9']['UTG+1'].update({  "UTG":      "88+, A7s+, KJs+, QJs, AQo+", 
                                "UTG+1":    "NONE", 
                                "MP":       "QQ+, AKs, AKo", 
                                "MP+1":     "QQ+, AJs+, KQs, AQo+", 
                                "HJ":       "QQ+, AJs+, KQs, AQo+", 
                                "CO":       "QQ+, AJs+, KQs, AQo+", 
                                "BU":       "QQ+, AJs+, KQs, AQo+", 
                                "SB":       "JJ+, AQs+, KQs, AKo",
                                "BB":       "JJ+, AQs+, KQs, AKo"
                            })
CALLING['9']['MP'].update({     "UTG":      "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "UTG+1":    "88+, A7s+, KJs+, QJs, AQo+", 
                                "MP":       "NONE", 
                                "MP+1":     "JJ+, ATs+, KQs, AQo+", 
                                "HJ":       "JJ+, ATs+, KQs, AQo+", 
                                "CO":       "JJ+, ATs+, KQs, AQo+", 
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo",
                                "BB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo"
                            })
CALLING['9']['MP+1'].update({   "UTG":      "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "UTG+1":    "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP":       "88+, A7s+, KJs+, QJs, AQo+", 
                                "MP+1":     "NONE", 
                                "HJ":       "JJ+, ATs+, KQs, AQo+", 
                                "CO":       "JJ+, ATs+, KQs, AQo+", 
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo",
                                "BB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo"
                            })
CALLING['9']['HJ'].update({     "UTG":      "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "UTG+1":    "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP+1":     "88+, A7s+, KJs+, QJs, AQo+",  
                                "HJ":       "NONE", 
                                "CO":       "JJ+, ATs+, KQs, AQo+", 
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo",
                                "BB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo"
                            })
CALLING['9']['CO'].update({     "UTG":      "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "UTG+1":    "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP+1":     "88+, A7s+, KJs+, QJs, AQo+", 
                                "HJ":       "88+, A7s+, KJs+, QJs, AQo+", 
                                "CO":       "NONE", 
                                "BU":       "QQ+, AKs, AKo", 
                                "SB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo",
                                "BB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo"
                            })
CALLING['9']['BU'].update({     "UTG":      "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "UTG+1":    "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo", 
                                "MP+1":     "88+, A7s+, KJs+, QJs, AQo+", 
                                "HJ":       "88+, A7s+, KJs+, QJs, AQo+", 
                                "CO":       "TT+, ATs+, KQs, QJs, AQo+", 
                                "BU":       "NONE", 
                                "SB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo",
                                "BB":       "55+, A2s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+, JTo"
                            })
CALLING['9']['SB'].update({     "UTG":      "QQ+, AKs, AKo", 
                                "UTG+1":    "QQ+, AKs, AKo", 
                                "MP":       "JJ+, AJs+, KQs, AKo", 
                                "MP+1":     "JJ+, AJs+, KQs, AKo", 
                                "HJ":       "TT+, AJs+, KQs, QJs, AKo", 
                                "CO":       "TT+, AJs+, KQs, QJs, AKo", 
                                "BU":       "TT+, AJs+, KQs, QJs, AKo", 
                                "SB":       "NONE",
                                "BB":       "22+, A2s+, KTs+, QTs+, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, A8o+, KTo+, QTo+, JTo, T9o, 98o"
                            })
CALLING['9']['BB'].update({     "UTG":      "QQ+, AKs, AKo", 
                                "UTG+1":    "QQ+, AKs, AKo", 
                                "MP":       "JJ+, AJs+, KQs, AKo", 
                                "MP+1":     "JJ+, AJs+, KQs, AKo", 
                                "HJ":       "TT+, AJs+, KQs, QJs, AKo", 
                                "CO":       "TT+, AJs+, KQs, QJs, AKo", 
                                "BU":       "TT+, AJs+, KQs, QJs, AKo", 
                                "BB":       "NONE"
                            })

CALLING['6']['UTG'].update({    "UTG":      "NONE", 
                                "MP":       "99+, ATs+, KQs, ATo+, KQo", 
                                "CO":       "66+, A8s+, KQs, QJs, JTs, ATo+, KQo",
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "99+, ATs+, KQs, ATo+, KQo",
                                "BB":       "99+, ATs+, KQs, ATo+, KQo"
                            })
CALLING['6']['MP'].update({     "UTG":      "99+, ATs+, KQs, ATo+, KQo", 
                                "MP":       "NONE",
                                "CO":       "66+, A8s+, KQs, QJs, JTs, ATo+, KQo", 
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "99+, ATs+, KQs, ATo+, KQo",
                                "BB":       "99+, ATs+, KQs, ATo+, KQo"
                            })
CALLING['6']['CO'].update({     "UTG":      "99+, ATs+, KQs, ATo+, KQo", 
                                "MP":       "66+, A8s+, KQs, QJs, JTs, ATo+, KQo", 
                                "CO":       "NONE", 
                                "BU":       "JJ+, ATs+, KQs, AQo+", 
                                "SB":       "99+, ATs+, KQs, ATo+, KQo",
                                "BB":       "99+, ATs+, KQs, ATo+, KQo"
                            })
CALLING['6']['BU'].update({     "UTG":      "66+, A8s+, KQs, QJs, JTs, ATo+, KQo", 
                                "MP":       "22+, A6s+, KQs, QJs, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, A8o+, KQo", 
                                "CO":       "22+, A5s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, A2o+, KQo, JTo", 
                                "BU":       "NONE", 
                                "SB":       "22+, A2s+, KTs+, QTs+, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, A2o+, KTo+, QTo+, JTo, T9o, 98o, 87o, 76o, 65o, 54o, 43o, 32o",
                                "BB":       "22+, A2s+, KTs+, QTs+, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, A2o+, KTo+, QTo+, JTo, T9o, 98o, 87o, 76o, 65o, 54o, 43o, 32o"
                            })
CALLING['6']['SB'].update({     "UTG":      "99+, ATs+, KQs, AQo+", 
                                "MP":       "44+, A8s+, KQs, QJs, JTs, T9s, 98s, 87s, AQo+", 
                                "CO":       "22+, A6s+, KJs+, QJs, JTs, T9s, 98s, 87s, 76s, 65s, AQo+", 
                                "BU":       "22+, A2s+, KTs+, QTs+, JTs, T9s, 98s, 87s, 76s, 65s, 54s, 43s, 32s, AQo+", 
                                "SB":       "NONE", 
                                "BB":       "55+, A2s+, KTs+, QTs+, J9s+, T8s+, 98s, 87s, 76s, 65s, ATo+, KTo+, QTo+, JTo"
                            })
CALLING['6']['BB'].update({     "UTG":      "22+, A7s+, K9s+, Q9s+, J9s+, T8s+, 98s, 87s, 76s, 65s, 54s, A9o+, KTo+, QTo+, JTo", 
                                "MP":       "22+, A5s+, K4s+, Q8s+, J7s+, T8s+, 97s+, 86s+, 75s+, 65s, 54s, A6o+, K9o+, QTo+, JTo, T9o", 
                                "CO":       "22+, A2s+, K2s+, Q5s+, J5s+, T6s+, 96s+, 86s+, 75s+, 64s+, 54s, A2o+, K7o+, Q9o+, J9o+, T8o+, 98o", 
                                "BU":       "22+, A2s+, K2s+, Q2s+, J4s+, T5s+, 95s+, 85s+, 75s+, 64s+, 53s+, A2o+, K2o+, Q4o+, J7o+, T7o+, 97o+, 86o+, 76o", 
                                "SB":       "22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 94s+, 85s+, 74s+, 63s+, 53s+, 43s, A2o+, K2o+, Q2o+, J2o+, T4o+, 96o+, 86o+, 75o+, 65o", 
                                "BB":       "NONE"
                            })
