		import tweepy
		 
		auth = tweepy.OAuthHandler('WOzuctnVvgJUbYPXErZnJIECs', 'D4u6VstKV7y5mwjOPDBUxFLFqgWy3uKT2u6qPPeDRM8ouilJpv')
		auth.set_access_token('766081496641900544-Yd6LZJRp9Gj6t1bZXD8McWvUmA18RdJ', 'vqvOWNWzrJ31CnPgTJ7Ik65T7MbZAyQf3avLjYfZOHTHm')
		 
		api = tweepy.API(auth)
		 
		api.update_status(status="Hmmm.")
		user = api.get_user()
		print ("User id: " + user.id_str)
		print (user.name)
		print ("Description: " + user.description)
		print ("Language: " + user.lang)
		print ("Account created at: " + str(user.created_at))
		print ("Location: " + user.location)
		print ("Time zone: " + user.time_zone)
		print ("Number of tweets: " + str(user.statuses_count))
		print ("Number of followers: " + str(user.followers_count))
		print ("Following: " + str(user.friends_count))
		print ("A member of " + str(user.listed_count) + " lists.")


		statuses = api.user_timeline(id = user.id, count = 200)
		 
		for status in statuses:
			print ("***")
			print ("Tweet id: " + status.id_str)
			print (status.text)
			print ("Retweet count: " + str(status.retweet_count))
			print ("Favorite count: " + str(status.favorite_count))
			print (status.created_at)
			print ("Status place: " + str(status.place))
			print ("Source: " + status.source)
			print ("Coordinates: " + str(status.coordinates))
			
			time.sleep(1)