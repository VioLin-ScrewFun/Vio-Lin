<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Web</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
            background: black;
        }
        .video-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
        }
        .content {
            position: relative;
            z-index: 1;
        }
    </style>
</head>
<body>
    <video autoplay loop class="video-background">
        <source src="https://drive.google.com/file/d/180qpY94izaU17Kqgbsmd5iJwIgGIMmAE/view?usp=sharing" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div class="content">
        <h1>¡Bienvenido a mi página web!</h1>
        <p>Esta página está en construcción.</p>
    </div>
</body>
</html>
