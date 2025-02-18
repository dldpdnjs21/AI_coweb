<?php
session_start();

$conn = mysqli_connect("jjn3912.iptime.org", "coweb", "@jjn7723912", "cowab") or die("DB에 연결할 수 없습니다.");

$userId = $_SESSION['userId'];

// 사용자 정보 가져오기
$sql_get_user_info = "SELECT * FROM user WHERE id = '{$userId}'";
$result_user_info = mysqli_query($conn, $sql_get_user_info);
$user_info = mysqli_fetch_array($result_user_info);
$user_name = $user_info['name'];
$user_assets = $user_info['money'];
$quantity = $user_info['btc'];

// BTC를 원화로 구매한 가격 (임시로 10만원으로 설정)
$buy_price = 100000;

$total_purchase_price = $buy_price;

// 현재 BTC 시세 가져오기
$price_json = file_get_contents("https://api.upbit.com/v1/ticker?markets=KRW-BTC");
$price_data = json_decode($price_json, true);
$price = $price_data[0]['trade_price']; // BTC의 현재 가격

$quantity = floor($total_purchase_price / $price);

// 사용자가 보유한 BTC를 원화로 환산한 총 가격
$btc_purchase_price = $quantity * $buy_price;

$user_assets -= $total_purchase_price;

// 총 보유 자산 계산
$total_assets = $user_assets + ($quantity * $price);

// 데이터베이스 업데이트
$sql_update_user_info = "UPDATE user SET money = '{$user_assets}', btc = '{$quantity}' WHERE id = '{$userId}'";
mysqli_query($conn, $sql_update_user_info);

?>

<!DOCTYPE html>
<html lang="ko">
<head>
    <link href="https://fonts.gooleapis.com/css?family=Noto+Sans+KR&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My page</title>
    <link rel="stylesheet" href="../css/main.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../css/mypage.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        const userId = '<?php echo $userId; ?>';
        let Quantity = <?php echo $quantity; ?>;
        let userAssets = <?php echo $user_assets; ?>;
        let totalPurchasePrice = <?php echo $total_purchase_price; ?>;

        function updateData() {
            fetch("https://api.upbit.com/v1/ticker?markets=KRW-BTC")
                .then(response => response.json())
                .then(data => {
                    const Price = data[0].trade_price; // BTC의 현재 가격

                    // 매수금액 업데이트
                    const totalPurchaseAmount = (Quantity * Price).toLocaleString() + " KRW";
                    document.getElementById("totalPurchaseAmount").innerText = totalPurchaseAmount;

                    // 평가손익 업데이트
                    const totalEvaluationAmount = ((Quantity * Price) - totalPurchasePrice).toLocaleString() + " KRW";
                    document.getElementById("totalEvaluationAmount").innerText = totalEvaluationAmount;

                    // 평가금액 업데이트
                    const totalProfitLoss = (userAssets + (Quantity * Price) - totalPurchasePrice).toLocaleString() + " KRW";
                    document.getElementById("totalProfitLoss").innerText = totalProfitLoss;

                    // 평가 수익률 업데이트
                    const totalProfitRate = ((((Quantity * Price) - totalPurchasePrice) / totalPurchasePrice) * 100).toFixed(2) + "%";
                    document.getElementById("totalProfitRate").innerText = totalProfitRate;

                })
                .catch(error => console.error("Error fetching BTC price:", error));
        }

        document.addEventListener("DOMContentLoaded", function() {
            updateData();
            setInterval(updateData, 1000);
        });
    </script>
    
</head>
<body>
<div class="wrap">
    <div class="intro_bg">
        <div class="header">
            <h2 class="logo"><span>C</span><span>o</span><span>w</span><span>e</span><span>b</span></h2>
            <ul class="nav">
                <li><a href="main.html">TRADE</a></li>
                <li><a href="#"></a>ABOUT</li>
                <li><a href="#"></a>MYPAGE</li>
                <li>
                    <button class="btnLogout">Logout</button>
                </li>
            </ul>
        </div>
        <div class="userpage_main">
            <section class="ty01">
                <article>
                    <div class="tabmenu_01">
                        <div class="tab_list">
                            <div class="MyTrade">
                                <div class="MyTrade__TradeState TradeState">
                                    <div class="profile">
                                        <img src="", width=50px, height=50px><h2><?php echo $user_name; ?></h2>
                                    </div>
                                    <div class="TradeState__section TradeState__section--amount">
                                        <div class="TradeAmount">
                                            <dl class="TradeAmount__row TradeAmount__row--total">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">보유 KRW</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count TradeAmount__count--total" id="userAssets"><?php echo number_format($user_assets); ?> KRW</span>
                                                </dd>
                                            </dl>
                                            <dl class="TradeAmount__row TradeAmount__row--total">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">총 보유자산</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count TradeAmount__count--total"><?php echo number_format($total_assets); ?><i class="TradeAmount__unit">KRW</i></span>
                                                </dd>
                                            </dl>


                                            <dl class="TradeAmount__row">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">총매수금액</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count"><?php echo number_format($total_purchase_price); ?><i class="TradeAmount__unit">KRW</i></span>
                                                </dd>
                                            </dl>
                                            <dl class="TradeAmount__row">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">총평가손익</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count TradeAmount__count--decrease"><?php echo number_format(($total_assets - $buy_price)); ?><i class="TradeAmount__unit">KRW</i></span>
                                                </dd>
                                            </dl>
                                            <dl class="TradeAmount__row">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">총평가금액</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count"><?php echo number_format($total_assets); ?><i class="TradeAmount__unit">KRW</i></span>
                                                </dd>
                                            </dl>
                                            <dl class="TradeAmount__row">
                                                <dt class="TradeAmount__TitleCell">
                                                    <span class="TradeAmount__title">총평가수익률</span>
                                                </dt>
                                                <dd class="TradeAmount__CountCell">
                                                    <span class="TradeAmount__count TradeAmount__count--decrease"><?php echo number_format(((($quantity * $price) - $buy_price) / $buy_price) * 100, 2); ?><i class="TradeAmount__unit">%</i></span>
                                                </dd>
                                            </dl>
                                        </div>
                                    </div>
                                </div>
                                <div class="AmontTable">
                                    <div class="AmountTable__Header">
                                        <h5 class="AmountTable__title">보유자산 목록</h5>
                                    </div>
                                    <table class="AmountTable__HeadTable">
                                        <thead>
                                        <tr>
                                            <th>보유자산</th>
                                            <th>보유수량</th>
                                            <th class="AmountTable__HeadTitle">
                                                <a href="#" class="">매수평균가 <img src="https://cdn.upbit.com/upbit-web/images/ico_sort.52f3f4e.png" alt=""></a>
                                            </th>
                                            <th class="AmountTable__HeadTitle">
                                                <a href="#" class="">매수금액 <img src="https://cdn.upbit.com/upbit-web/images/ico_sort.52f3f4e.png" alt=""></a>
                                            </th>
                                            <th class="AmountTable__HeadTitle"><a href="#" class="selected">평가금액 <img src="https://cdn.upbit.com/upbit-web/images/ico_sort.52f3f4e.png" alt=""></a>
                                            </th>
                                            <th class="AmountTable__HeadTitle"><a href="#" class="">평가손익(%) <img src="https://cdn.upbit.com/upbit-web/images/ico_sort.52f3f4e.png" alt=""></a>
                                            </th>

                                        </tr>
                                        </thead>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </article>
            </section>
            <section class="ty02">
                <div class="trade">
                    <div class="Search">
                        <div class="Search_con">
                            <input type="search" id="search" placeholder="Search..." />
                        </div>
                        <div class="Search_bar">
                            <span class="S-icon"><i class="fa fa-search"></i></span>
                        </div>
                    </div>
                    <!-- 코인 리스트 -->
                    <div class="header_fixed">
                        <table class="coinList">
                            <thead>
                            <tr>
                                <th>Coin</th>
                                <th>Price<button id="sort-price-desc" class="sort-btn">▼</button><button id="sort-price-asc" class="sort-btn">▲</button></th>
                                <th>Range(day)<button id="sort-range-desc" class="sort-btn">▼</button><button id="sort-range-asc" class="sort-btn">▲</button></th>
                                <th>Total</th>
                            </tr>
                            </thead>
                            <tbody>
                            <!--  API에서 받아온 데이터  -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>
        </div>
    </div>
    <div class="footer">
        <div>Coweb</div>
        <div>
            Dev. 김동해, 이규민, 이예원 <br>
            Tel. 02 - 123 -3456 <br>
            COPYRIGHT 2024. ALL RIGHT RESERVED.
        </div>
    </div>
</div>
<script src="../js/loginPopup.js"></script>
<script src="../js/coinList.js"></script>
<script src="../js/coinChart.js"></script>
<script src="../js/coinChart2.js"></script>
<script src="../js/coinTable.js"></script>
</body>
</html>
