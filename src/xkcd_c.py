from base_command import BaseCommand
from xkcd import getComic, getLatestComic, getRandomComic
class Xkcd(BaseCommand):
    name = "xkcd"
    description = "show a random (or not) XKCD comic"

    async def run(self, client, message, args):
        if len(args) == 0:
            comic = getLatestComic()
        elif len(args) > 0:
            try:
                num = int(args[0])
            except:
                await message.channel.send("Nice try asshole, floats arent real.")
                return
            
            comic = getComic(num)
        
        if "imageLink" not in dir(comic):
            await message.channel.send("That is not a valid XKCD comic!")
            return 
        
        await message.channel.send(f"{comic.getImageLink()}")
        return