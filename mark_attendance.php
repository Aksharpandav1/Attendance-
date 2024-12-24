<?php
include 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $serial = $_POST['serial'];
    $date = date('Y-m-d');
    
    $sql = "INSERT INTO attendance (serial_number, date, status) VALUES ('$serial', '$date', 'Present')";
    if ($conn->query($sql) === TRUE) {
        echo "Attendance marked!";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

{% extends 'base.html' %}
{% block content %}
<div class="container mt-4">
    <h2>Mark Attendance</h2>

    <!-- Search Form -->
    <form method="get" action="/mark-attendance" class="mb-3">
        <div class="input-group">
            <input type="text" name="search" class="form-control" placeholder="Search by Name or Serial Number" value="{{ search_query }}">
            <button class="btn btn-primary" type="submit">Search</button>
        </div>
    </form>

    <!-- Attendance Form -->
    <form method="post" action="/mark-attendance">
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Serial Number</th>
                    <th>Name</th>
                    <th>Address</th>
                    <th>Position</th>
                    <th>Mark Attendance</th>
                </tr>
            </thead>
            <tbody>
                {% for devotee in devotees %}
                <tr>
                    <td>{{ devotee.serial_number }}</td>
                    <td>{{ devotee.name }}</td>
                    <td>{{ devotee.address }}</td>
                    <td>{{ devotee.position }}</td>
                    <td>
                        <input type="checkbox" name="attendance" value="{{ devotee.id }}">
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <button class="btn btn-success mt-3" type="submit">Submit Attendance</button>
    </form>
</div>
{% endblock %}
