# hatebpy

hatebpyは、はてなブックマークAPIを簡単に利用するためのPythonライブラリです。

## 特徴

- はてなブックマークAPIの主要機能をサポート
- 簡単な認証プロセス
- タイプヒントによる型安全性
- フィード検索機能

## インストール

pipを使用してインストールできます：

```bash
pip install hatebpy
```

## 使用方法

### 認証

はてなブックマークAPIを使用するには、OAuthによる認証が必要です。以下のコマンドを実行して認証を行います：

```bash
hatebpy <consumer_key> <consumer_secret>
```

### 基本的な使用例

```python
from hatebpy import HatenaBookmarkClient, OAuth1Auth

# クライアントの初期化
auth = OAuth1Auth(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
client = HatenaBookmarkClient(auth)

# ブックマークの取得
bookmark = client.get_bookmark("https://example.com")
print(bookmark)

# ブックマークの更新
updated_bookmark = client.update_bookmark(
    url="https://example.com",
    comment="example.com test",
    tags=["example", "test"]
)
print(updated_bookmark)
```

より詳細な使用方法については、[使用方法のドキュメント](docs/usage.md)を参照してください。

## 開発

### 依存関係のインストール

```bash
pip install -r requirements.txt
```

### テストの実行

```bash
pytest
```

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 貢献

バグ報告、機能リクエスト、プルリクエストなど、あらゆる形での貢献を歓迎します。大きな変更を加える前に、まずissueを開いて議論してください。

## 作者

K(rmc-8.com)

## 謝辞

- はてなブックマークAPIを提供してくださっているはてな株式会社に感謝します。
