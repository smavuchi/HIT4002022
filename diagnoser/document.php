<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:m="http://schemas.microsoft.com/office/2004/12/omml" xmlns="http://www.w3.org/TR/REC-html40">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Medical report - Diagnoser</title>
    <!--[if gte mso 9]>
    <xml>
    <w:WordDocument>
    <w:View>Print
    <w:Zoom>100
    <w:DoNotOptimizeForBrowser/>
    </w:WordDocument>
    </xml>
    <![endif]-->
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i">
    <link rel="stylesheet" href="assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/fonts/font-awesome.min.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome5-overrides.min.css">
</head>

<body id="page-top">
    <div id="wrapper">
        <div class="d-flex flex-column" id="content-wrapper">
            <div class="mt-5" id="content">
                <div class="container-fluid">
                    <div class="d-sm-flex justify-content-between align-items-center mb-4">
                        <h3 class="text-dark mb-0">Medical report</h3>

                    </div>
                    <div id="reportcontent" class="row mb-3">
                        <div class="col-md-4">
                            <div class="row">
                                <div class="col">
                                    <div class="card shadow mb-3">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 fw-bold">Patient details</p>
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
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/theme.js"></script>
</body>

</html>