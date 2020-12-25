import tweepy
auth = tweepy.OAuthHandler("QEm5qWrK3RmA2ISmySSLzbmMO", "agOmwdAbKaSqmZKMrTQLY9wD1eLBZnUz0m42KBYedHM9MwSLfD")
auth.set_access_token("1337028960526295041-9nn2oMIu2cmhxnz1avOiAvmGH2O6DQ", "vvoUy1aqtu30ZB0br2za9G4DTFMgzHrlWa3L5hhBZ8nYT")
api = tweepy.API(auth)
print ("tweet message!")
print ("twitter for?")
tweet = input("ketik sebuah tweet ")
api.update_status(status = (tweet))
print ("done")