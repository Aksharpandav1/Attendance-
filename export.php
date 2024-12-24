<?php
include 'db.php';

header("Content-Type: application/xls");
header("Content-Disposition: attachment; filename=attendance_records.xls");

$sql = "SELECT * FROM attendance";
$result = $conn->query($sql);

echo "Serial Number\tDate\tStatus\n";
while ($row = $result->fetch_assoc()) {
    echo $row['serial_number'] . "\t" . $row['date'] . "\t" . $row['status'] . "\n";
}
?>
