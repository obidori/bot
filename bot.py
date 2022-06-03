import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="문의 하지마"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

  
 @client.event
 module.exports = {
    name:"티켓",
    async execute(message){
        if(message.channel.type !== "GUILD_TEXT") return
        const channel = await message.guild.channels.create('TIKET : ${message.author.tag}')
        message.delete()

        channel.permissionOverwrites.edit(message.guild.id , {
            SEND_MESSAGES : false,
            VIEW_CHANNEL: false
        })

        channel.permissionOverwrites.edit(message.author,{
            VIEW_CHANNEL:true,
            SEND_MESSAGES:true
        })
        const msg = await message.reply('**아래 채널로 이동해주세요! ${channel}**')
        const reactionmsg = await channel.send('**문의하실 내용을 적어주세요 !**')

        await reactionmsg.react("❌")

        const collector = reactionmsg.createReactionCollector()

        collector.on("collect", (reaction,user)=>{
            switch(reaction.emoji.name){
                case "❌" :
                channel.send("**채널이 3초뒤 삭제됩니다**")
                setTimeout(() => { channel.delete() }, 3000);
                setTimeout(() => { msg.delete() }, 3000);
                break;

                
            }
        })
    }
}            

client.run(os.environ['token'])
