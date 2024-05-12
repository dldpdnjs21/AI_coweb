<?php
session_start();

$conn = mysqli_connect("jjn3912.iptime.org","coweb","@jjn7723912","cowab") or die ("Can't access DB");

$userId = $_SESSION['userId'];

$quantity=$_POST['quantity'];
$price=$_POST['price'];
$transactionType = $_POST['transactionType'];

$total = $quantity * $price;

$sql_insert_transaction = "INSERT INTO transaction (user_id, quantity, price, total, type, transaction_time) 
                          VALUES ('$userId', '$quantity', '$price', '$total', '$transactionType', NOW())";
$result_insert_transaction = mysqli_query($conn, $sql_insert_transaction);

if($transactionType === "buy"){
    $sql_update_balance = "UPDATE user SET balance = balance - $total WHERE id = '$userId'";
} else if($transactionType === "sell") {
    $sql_update_balance = "UPDATE user SET balance = balance + $total WHERE id = '$userId'";
}

$result_update_balance = mysqli_query($conn, $sql_update_balance);

$response = array();
if ($result_insert_transaction && $result_update_balance) {
    $response['success'] = true;
} else {
    $response['success'] = false;
    $response['error'] = "거래 처리 중 오류가 발생하였습니다.";
}

header("Content-Type: application/json");
echo json_encode($response);

?>