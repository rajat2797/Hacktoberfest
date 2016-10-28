var backgroundcolor=[
  {
    "imglink": "http://webneel.com/wallpaper/sites/default/files/images/04-2013/gorgeous-beach-wallpaper.jpg",
    "color": "#4d94ff" 
  },
   {
    "imglink" : "http://webneel.com/wallpaper/sites/default/files/images/04-2013/tropical-beach-wallpaper.jpg" ,
    "color":  "#1affff",
   },
  {
    "imglink": "http://webneel.com/wallpaper/sites/default/files/images/04-2013/natural-scenery-wallpaper.jpg",
    "color": "#446600"
  },
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/14-beach-sea-photography.jpg",
    "color":"#992600",
  },
  {
  "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/16-beach-sea-photography.jpg",
    "color":"#4da6ff"
  },
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/22-beach-sea-photography.jpg",
    "color":"#751aff"
  },
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/30-beautiful-sunrise.jpg",
    "color":"#264d00"
  },
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/31-beautiful-sunrise.jpg",
    "color":"#994d00"
  },
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/28-beautiful-sunrise.jpg",
    "color":"#3d0066"
  }
  ,
  {
    "imglink":"http://webneel.com/wallpaper/sites/default/files/images/04-2013/23-beautiful-sunrise.jpg",
    "color":"#330a00"
  }
    
  
];
var currentQuote="";
var currentAuthor="";
function getquote()
{
  $.ajax({
  headers: {
      "X-Mashape-Key": "OivH71yd3tmshl9YKzFH7BTzBVRQp1RaKLajsnafgL2aPsfP9V",
      Accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
    },
    url: "https://andruxnet-random-famous-quotes.p.mashape.com/cat=",
    success: function(response) {
      var r = JSON.parse(response);
      currentQuote = r.quote;
      currentAuthor = r.author;
      
   $("#text").text(r.quote);
   $("#authorname").text(r.author);
      
      var indez= Math.floor(Math.random()*backgroundcolor.length);
   $('html body').css("background","transparent url('"+backgroundcolor[indez].imglink.replace()+"') no-repeat center center"); 
     $(".buttons").css("color",backgroundcolor[indez].color);
}
});
}
$(document).ready(function(){
  getquote();
  $("#newquote").click(getquote);
});