<?php
$conn = mysqli_connect("jjn3912.iptime.org","coweb","@jjn7723912","cowab") or die ("Can't access DB");
$hashedPassword =hash('sha256',$_POST['pass']);
$sql = "
    INSERT INTO user
    (id, name, pass)
    VALUES('{$_POST['email']}','{$_POST['name']}','{$hashedPassword}'
    )";
$result = mysqli_query($conn, $sql);

if ($result === false) {
    echo "저장에 문제가 생겼습니다. 관리자에게 문의해주세요.";
    echo mysqli_error($conn);
} else {
?>
    <script>
        alert("회원가입이 완료되었습니다");
        location.href = "loginregister.html";
    </script>
<?php
}
?>