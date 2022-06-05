<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Profile - Diagnoser</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i">
    <link rel="stylesheet" href="assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/fonts/font-awesome.min.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome5-overrides.min.css">
    <link rel="stylesheet" href="assets/css/Application-Form.css">
</head>

<body onload="predictOnPageLoad()" id="page-top">
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
                    <li class="nav-item"><a href="./doctorhome.php" class="btn btn-outline-light d-none d-sm-inline-block" role="button" href="#">
                            <i class="fas fa-arrow-left"></i>&nbsp;Back</a></li>
                    <li class="nav-item"><br></li>
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
                    <div class="d-sm-flex justify-content-between align-items-center mb-4">
                        <h3 class="text-dark mb-0">Patient details</h3>
                        <div id="notif"></div><a onclick="generatereport()" class="btn btn-primary d-none d-sm-inline-block" role="button" href="#">
                            <i class="fas fa-file-medical"></i>&nbsp;Generate report</a>
                    </div>
                    <div id="reportcontent" class="row mb-3">
                        <div class="col-md-4">
                            <div class="row">
                                <div class="col">
                                    <div class="card shadow mb-3">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 fw-bold">Medical report</p>
                                        </div>
                                        <?php
                                        $con = mysqli_connect("localhost", 'root', '', 'diagnoser');
                                        $image = null;
                                        $diagnosis = null;
                                        $probabilities = null;
                                        $result = mysqli_query($con, "SELECT * FROM bookings WHERE id=" . $_GET['id']);
                                        while ($row = mysqli_fetch_array($result)) {
                                            $image = $row['xrayimage'];
                                            $diagnosis = $row['diagnosis'];
                                            $probabilities = $row['probabilities'];
                                        ?>
                                            <div class="card-body">
                                                <div class="row">
                                                    <div class="col">
                                                        <h6 style="color: black;" class="mb-2"><strong>Name: <?php echo $row['firstname']; ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>Surname: <?php echo $row['lastname']; ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>DOB: <?php echo $row['dob']; ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>Age:<?php echo (date_diff(date_create($row['dob']), date_create(date("Y-m-d"))))->format('%y'); ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>Email: <?php echo $row['email']; ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>Phonenumber: <?php echo $row['phonenumber']; ?></strong></h6>
                                                        <h6 style="color: black;" class="mb-2"><strong>Address: <?php echo $row['address']; ?></strong></h6>
                                                    </div>
                                                </div>
                                            </div>
                                        <?php
                                        }
                                        ?>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="row">
                                <div class="col">
                                    <div class="card shadow mb-3">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 fw-bold">X-ray scan results</p>
                                        </div>
                                        <div class="card-body">
                                            <div class="row">
                                                <div class="col">
                                                    <img src="<?php echo $image; ?>" id="selected-image" style="max-width: 400px;" height="400" alt="No xray image uploaded">
                                                </div>
                                                <div class="col">
                                                    <p style="font-weight: bold;font-size: 35px;color: black;">Diagnosis</p>
                                                    <span style="color: black;font-size: 20px;" id="diagnosis"><?php echo $diagnosis; ?></span>
                                                    <br>
                                                    <p class="mt-3" style="font-weight: bold;font-size: 35px;color: black;">Probabilities</p>
                                                    <h5 style="color: black;" class='w3-left-align text-color' id='prediction-list'><?php echo $probabilities; ?></h5>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div style="display:none">
        <button id='predict-button'>Predict</button>
    </div>
    <div style="display:none">
        <input id="image-selector" type="file" multiple>
    </div>

    <script src="assets/js/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.13.3/dist/tf.min.js"></script>
    <script src="./assets/js/target_classes.js"></script>
    <script src="./assets/js/app_startupp.js"></script>
    <script src="./assets/js/imagerecog.js"></script>
    <script>
        function generatereport() {
            var reportcontent = $("#reportcontent").html();
            var printWindow = window.open('', 'PRINT', 'height=400,width=800');
            printWindow.document.write('<!DOCTYPE html><html><head>' +
                '<meta charset="utf-8">' +
                '<meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">' +
                '<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">' +
                '</head><body >');
            printWindow.document.write(reportcontent);
            printWindow.document.write('</body></html>');
            printWindow.document.close();
            printWindow.focus();
            setInterval(function () {
                       printWindow.print();
                    }, 2000);
                    printWindow.document.close();
                    return true;
           
        }
    </script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/theme.js"></script>


</body>

</html>