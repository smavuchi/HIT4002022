<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Blank Page - Diagnoser</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i">
    <link rel="stylesheet" href="assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/fonts/font-awesome.min.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome5-overrides.min.css">
    <link rel="stylesheet" href="assets/css/Application-Form.css">
</head>

<body id="page-top">
    <div id="wrapper">
        <nav class="navbar navbar-dark align-items-start sidebar sidebar-dark accordion bg-gradient-primary p-0">
            <div class="container-fluid d-flex flex-column p-0"><a class="navbar-brand d-flex justify-content-center align-items-center sidebar-brand m-0" href="#">
                    <div class="sidebar-brand-icon rotate-n-15"><i class="fas fa-laugh-wink"></i></div>
                    <div class="sidebar-brand-text mx-3"><span>Diagnoser</span></div>
                </a>
                <hr class="sidebar-divider my-0">
                <ul class="navbar-nav text-light" id="accordionSidebar">
                    <li class="nav-item"></li>
                    <li class="nav-item"></li>
                    <li class="nav-item"></li>
                    <li class="nav-item"></li>
                    <li class="nav-item"></li>
                    <li class="nav-item">
                        <a href="index.html" class="btn btn-outline-light d-none d-sm-inline-block" role="button" href="#">
                            <i class="far fa-arrow-alt-circle-left"></i>&nbsp;Logout</a>
                    </li>
                </ul>

            </div>
        </nav>
        <div class="d-flex flex-column" id="content-wrapper">
            <div id="content">
                <nav class="navbar navbar-light navbar-expand bg-white shadow mb-4 topbar static-top">
                    <div class="container-fluid"><button class="btn btn-link d-md-none rounded-circle me-3" id="sidebarToggleTop" type="button"><i class="fas fa-bars"></i></button>
                        <h2 style="color: rgb(0,0,0);">Doctor</h2>
                        <form class="d-none d-sm-inline-block me-auto ms-md-3 my-2 my-md-0 mw-100 navbar-search">
                            <div class="input-group"></div>
                        </form>
                        <ul class="navbar-nav flex-nowrap ms-auto">
                            <li class="nav-item dropdown d-sm-none no-arrow"><a class="dropdown-toggle nav-link" aria-expanded="false" data-bs-toggle="dropdown" href="#"><i class="fas fa-search"></i></a>
                                <div class="dropdown-menu dropdown-menu-end p-3 animated--grow-in" aria-labelledby="searchDropdown">
                                    <form class="me-auto navbar-search w-100">
                                        <div class="input-group"><input class="bg-light form-control border-0 small" type="text" placeholder="Search for ...">
                                            <div class="input-group-append"><button class="btn btn-primary py-0" type="button"><i class="fas fa-search"></i></button></div>
                                        </div>
                                    </form>
                                </div>
                            </li>

                        </ul>
                    </div>
                </nav>
                <div class="container-fluid">
                    
                    <div class="row">
                        <!-- <div class="col-md-6">
                            <div class="card shadow mb-4 ">
                                <div class="card-header py-3">
                                    <h6 class="text-primary fw-bold m-0">Pending</h6>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <?php
                                    $con = mysqli_connect("localhost", 'root', '', 'diagnoser');
                                    $result = mysqli_query($con, "SELECT * FROM bookings WHERE status='pending'");
                                    while ($row = mysqli_fetch_array($result)) {
                                    ?>
                                        <li class="list-group-item">
                                            <div class="row align-items-center no-gutters">
                                                <div class="col me-2">
                                                    <h4 class="mb-0"><strong><?php echo $row['firstname'] . " " . $row['lastname']; ?></strong></h4>
                                                    <span>Scheduled for: <?php echo $row['doa']; ?></span>
                                                </div>
                                                <div class="col-auto"><a class="btn btn-secondary btn-icon-split" href="profile.php?id=<?php echo $row['id'] ?>" role="button"><span class="text-white-50 icon" style="background: var(--bs-orange);"><i class="fas fa-exclamation-circle" style="color: rgb(255,255,255);font-size: 20px;"></i></span><span class="text-white text">Open file</span></a></div>
                                            </div>
                                        </li>
                                    <?php
                                    }
                                    ?>
                                </ul>
                            </div>
                        </div> -->
                        <div class="col-md-6">
                            <div class="card shadow mb-4 ">
                                <div class="card-header py-3">
                                    <h6 class="text-primary fw-bold m-0"></h6>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <?php
                                    $con = mysqli_connect("localhost", 'root', '', 'diagnoser');
                                    $result = mysqli_query($con, "SELECT * FROM bookings WHERE status='complete'");
                                    while ($row = mysqli_fetch_array($result)) {
                                    ?>
                                        <li class="list-group-item">
                                            <div class="row align-items-center no-gutters">
                                                <div class="col me-2">
                                                    <h6 class="mb-0"><strong><?php echo $row['firstname'] . " " . $row['lastname']; ?></strong></h6>
                                                    <span>Scheduled for: <?php echo $row['doa']; ?></span>
                                                </div>
                                                <div class="col-auto"><a class="btn btn-secondary btn-icon-split" href="report.php?id=<?php echo $row['id'] ?>" role="button"><span class="text-white-50 icon" style="background-color: #0080ff;font-size: 20px;color: rgb(255,255,255);"><i class="fas fa-file-medical-alt" style="color: rgb(255,255,255);"></i></span><span class="text-white text">Open file</span></a></div>
                                            </div>
                                        </li>
                                    <?php
                                    }
                                    ?>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><a class="border rounded d-inline scroll-to-top" href="#page-top"><i class="fas fa-angle-up"></i></a>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/Application-Form-1.js"></script>
    <script src="assets/js/Application-Form.js"></script>
    <script src="assets/js/theme.js"></script>
</body>

</html>