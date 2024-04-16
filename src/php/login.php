<?php
$conn = mysqli_connect("jjn3912.iptime.org","coweb","@jjn7723912","cowab") or die ("Can't access DB");
//아이디 비교와 비밀번호 비교가 필요한 시점이다.
// 1차로 DB에서 비밀번호를 가져온다 
// 평문의 비밀번호와 암호화된 비밀번호를 비교해서 검증한다.
$email = $_POST['email'];
$password = hash('sha256',$_POST['pass']);
// DB 정보 가져오기 
$sql = "SELECT * FROM user WHERE id ='{$email}'";
$result = mysqli_query($conn, $sql);

$row = mysqli_fetch_array($result);
$hashedPassword = $row['pass'];
$row['id'];
echo $row['pass'];
echo $row['id'];
// DB 정보를 가져왔으니 
// 비밀번호 검증 로직을 실행하면 된다.
if ($row['pass'] === $password) {
    // 로그인 성공
    // 세션에 id 저장
	$sqllog = "INSERT INTO loginlog(id,status,time) values ('{$email}','Success',now())";
	$logresult = mysqli_query($conn, $sqllog);
    session_start();
    $_SESSION['userId'] = $row['id'];
    
?>
    <script>
        alert("로그인에 성공하였습니다.")
        location.href = "loginregister.html";
    </script>
<?php
} else {
    // 로그인 실패 
	$sqllog = "INSERT INTO loginlog(id,status,time) values ('{$email}','Fail',now())";
	$logresult = mysqli_query($conn, $sqllog);
?>
    <script>
        alert("로그인에 실패하였습니다");
		location.href = "loginregister.html";
    </script>
<?php
}
?>