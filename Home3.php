<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<link type="text/css" rel="stylesheet" href="css/bootstrap.css" />
<script src="js/jquery.js"></script>
<script src="js/bootstrap.js"></script>
</head>

<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-danger navbar-fixed-top">
<a href="#" class="navbar-brand" ></a>

<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#menubar"><span class="navbar-toggler-icon"></span></button>
<div class="collapse navbar-collapse" id="menubar">
 
 
<ul class="navbar-nav">
<li class="nav-item">
<a href="slider.php" class="nav-link active">Home</a>
</li>
<li class="nav-item dropdown">
<a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Registration</a>
<div class="dropdown-menu bg-danger" style="background-color:#003366;">
<a href="#" class="dropdown-item">Insert</a>
<a href="#" class="dropdown-item">Update</a>
<a href="#" class="dropdown-item">Delete</a>
</div>

</li>
<li class="nav-item">
<a href="#" class="nav-link">Services</a>
</li>
<li class="nav-item">
<a href="#" class="nav-link">Contact Us</a>
</li>
</ul>
</div>
</nav>
<!-------------------------------------------------------------------->
<div class="container-fluid">
<div class="row well" style="background-color:#FFFFCC;"   >
<div class="col-sm-2" align="center">
<img src="pictures/mother.jpg" style="margin-top:20px;"  class="img-circle  img-responsive"  />
</div>
<div class="col-sm-8" align="center" >
<p style="font-size:26px; color:#CC0000;" ><b> BANARAS HINDU UNIVERSITY</b> </p>
<p style="font-size:32px; color:#CC0000;" ><b>ISO 9001:1916 Certicate</b> </p>
<p style="font-size:16px ; color:#CC0000;" >ESTABLISHED(1916)</p>
</div>
<div class="col-sm-2" align="center">
<img src="pictures/reg.jpg" style="margin-top:20px;"  class="img-circle img-responsive "  />
</div>
</div>
</div>


  <!---------------------------------------------------------------------> 
   <div class="row">
      <div class="col-sm-6">
      <div class="carousel slide" data-ride="carousel" id="hum">
      
       <ol class="carousel-indicators">
       <li data-slide-to="0" class="active"></li>
        <li data-slide-to="1"></li>
         <li data-slide-to="2"></li>
          <li data-slide-to="3"></li>
       
       </ol>
      <div class="carousel-inner">
      <div class="carousel-item active">
      <img src="image/bhu5.jpg" height="400" width="800" style="margin-top:20px;" />
      <div class="carousel-caption">
      <marquee dir="ltr" scrolldelay="1"> <p><font size="+1" color="#FF0000">Welcome To Banaras Hindu University</font></p></marquee>
      </div>
      
      </div>
      
       <div class="carousel-item">
      <img src="image/bhu4.jpg" height="400" width="800"  style="margin-top:20px;" />
      <div class="carousel-caption">
     <marquee dir="ltr" scrolldelay="1"> <p><font size="+1" color="#FF0000">Welcome To Banaras Hindu University</font></p></marquee>
      </div>
      </div>
      
       <div class="carousel-item">
      <img src="image/bhu7.jpg" height="400" width="800"  style="margin-top:20px;" />
      <div class="carousel-caption">
      <marquee dir="ltr" scrolldelay="1"> <p><font size="+1" color="#FF0000">Welcome To Banaras Hindu University</font></p></marquee>
      </div>
      </div>
       <div class="carousel-item">
      <img src="image/bhu9.jpg" height="400" width="800"  style="margin-top:20px;" />
      <div class="carousel-caption">
      <marquee dir="ltr" scrolldelay="1"> <p><font size="+1" color="#FF0000">Welcome To Banaras Hindu University</font></p></marquee>
      </div>
      </div>
      
      </div>
      
      <a href="#hum" class="carousel-control-prev" data-slide="prev"><span class="carousel-control-prev-icon"></span></a>
      
      
        <a href="#hum" class="carousel-control-next" data-slide="next"><span class="carousel-control-next-icon"></span></a>
      </div>
     </div>
<!------------------------------------------------------------->


<div class="col-sm-6" >
<div class="card " style="margin-top:20px;">
<div class="card-heading " style="background-color:#CC0000; ">
<h1 align="center"><font color="#FFFFFF" size="+3"> About University</font></h1>
</div>
<div class="card-body" style=" background-color:#CCCCCC; border:#000000 1px solid;">
<p style="color:#000066; font-size:16px;"><marquee  direction="up" scrolldelay="200"><b> Banaras Hindu University located in Varanasi ,Uttar Pradesh. Established in 1916 by Pandit Madan Mohan Malaviya,BHU is the largest resedental university in Asia , with over 35,000 students.The university's main campus spread over 1,300 acres was build on land donated by the Kashi Naresh,the hereditary ruler of Banaras.The university is also planning to set up a campus in Bihar.BHU is organised into 6 institutes and 14 streams and about 140 department.</b> </marquee></p>
</div>

 <div class="card-body" align="center" style=" background-color:#CCCCCC; border:#000000 1px solid; ">
 <button type="button" class="btn btn-danger active  " data-toggle="modal" data-target="#hum">Website</button>
   
       <div class="modal" role="dialog"  id="hum" >
       
          <div class="modal-dialog modal-lg">
             <div class="modal-content">
             
               <div class="modal-header">
               <button type="buttton" class="close" data-dismiss="modal" >&times;</button>
              
                             
               </div>
               <div class="modal-body">
                      <form name="" action="welcome.php" method="get">
                      <div class="well">
                      <div class="form-group">
                      <label >Enter Your E-mail Id</label>
                        <input type="text" class="form-control" name="fname" />
                        </div>
                        <div class="form-group">
                      <label > Enter Your Password</label>
                        <input type="Password" class="form-control" name="pass" />
                        </div>
                       </div> <!--well closes-->
                       <div class="modal-footer">
                    <button type="buttton" class="btn btn-danger" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-success" >Login</button>
                    </div><!--modal footer closes-->
             
                      </form>
                    </div><!--modal body closes-->
                    
                    
                    
             </div>
          
          
          </div>
       
       
       </div>
   
   
   
   
 </div>
</div>
</div>
</div>
</div></div><br /> 



<!---------------header end----->
<div class="container-fluid">
<div class="row " style="background-color:#666666;">
<div class="col-sm-3" align="center">
<h1 style="color:#000000;">Contact Us</h1>
 <p> <span class="glyphicon glyphicon-earphone" style="color:#FFFFFF; font-size:28px;"></span><font color="#FFFFFF">+91 8948773645</font></p>
           <p> <span class="glyphicon glyphicon-envelope" style="color:#FFFFFF; font-size:28px;"></span><font color="#FFFFFF" >samjanagupta991836@gmail.com</font></p>
</div>
<div class="col-sm-3" align="center">
<h1 style="color:#000000;"> Useful Links</h1>
<p> <ul>
 <li> <a href=" http://www.google.com"><font  color="#FFFFFF"> www.Google.com</font></a></li>
<li> <a href=" http://www.gmail.com"><font  color="#FFFFFF"> www.Gmail.com</font></a></li>
</ul></p>
</div>
<div class="col-sm-6" align="center">
<h2 style="color:#000000; size:34px;" > Social Networking</h2>
<marquee  dir="ltr" scrolldelay="1" ><p style="color:#FFFFFF; size:12px;"> A social networking servise is an online plateform which people use to build social network or social relations with other people. </p></marquee>

<i class="fa fa-facebook-official" style="color:#000000; font-size:50px;" ></i>&nbsp;
 <i class="fa fa-twitter-square" style="color:#000000; font-size:50px;" ></i>&nbsp;
 <i class="fa fa-google-plus-square" style="color:#000000; font-size:50px;" ></i>&nbsp;
 <i class="fa fa-instagram" style="color:#000000; font-size:50px;" ></i>&nbsp;

</div>

</div>
</div>


</body>
</html>
