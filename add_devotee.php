<?php
include 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $serial = $_POST['serial'];
    $name = $_POST['name'];
    $address = $_POST['address'];
    $position = $_POST['position'];
    $contact = $_POST['contact'];

    $sql = "INSERT INTO devotees (serial_number, name, address, position, contact)
            VALUES ('$serial', '$name', '$address', '$position', '$contact')";

    if ($conn->query($sql) === TRUE) {
        echo "Devotee added successfully!";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<h2>Add Devotee</h2>
<form method="post">
    Serial Number: <input type="text" name="serial" required><br>
    Name: <input type="text" name="name" required><br>
    Address: <textarea name="address"></textarea><br>
    Position: 
    <select name="position">
        <option value="Devotee">Devotee</option>
        <option value="Karyakar">Karyakar</option>
    </select><br>
    Contact: <input type="text" name="contact"><br>
    <input type="submit" value="Add Devotee">
</form>
<p>Crafted by Akshar Pandav and guided by Mayur Pandav</p>
