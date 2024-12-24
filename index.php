<?php
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_id = $_POST['user_id'];
    $password = $_POST['password'];

    if ($user_id == 'Mayur Pandav' && $password == 'mayur1234') {
        $_SESSION['user'] = $user_id;
        header('Location: dashboard.php');
    } else {
        $error = "Invalid credentials!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login - Attendance System</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        <label>User ID:</label>
        <input type="text" name="user_id" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    <?php if (isset($error)) echo "<p>$error</p>"; ?>
    <p>Crafted by Akshar Pandav and guided by Mayur Pandav</p>
</body>
</html>
