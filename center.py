import movie_time
import fresh_tomatoes


toy_story = movie_time.Movie("Toy Story-3", "Story of a boy whose toys come to life", "https://www.movieposter.com/posters/archive/main/204/MPW-102287", "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avengers = movie_time.Movie("Avengers Infinity War-1", "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos", "https://i.ytimg.com/vi/pVxOVlm_lE8/maxresdefault.jpg", "https://www.youtube.com/watch?v=QwievZ1Tx-8")

#  print(toy_story.story_line)
#  toy_story.show_trailer()
#  print(avengers.story_line)

mov = [toy_story, avengers, avengers, avengers]

fresh_tomatoes.open_movies_page(mov)



