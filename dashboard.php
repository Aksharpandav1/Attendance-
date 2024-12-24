<?php
session_start();
if (!isset($_SESSION['user'])) {
    header('Location: index.php');
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h2>Welcome, <?php echo $_SESSION['user']; ?></h2>
    <ul>
        <li><a href="add_devotee.php">Add Devotee</a></li>
        <li><a href="mark_attendance.php">Mark Attendance</a></li>
        <li><a href="export.php">Export Records</a></li>
        <li><a href="logout.php">Logout</a></li>
    </ul>
    <p>Crafted by Akshar Pandav and guided by Mayur Pandav</p>
</body>
</html>
