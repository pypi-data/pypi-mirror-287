# Aliyun API Python
一个简单的阿里云API Python封装库与SDK
## 使用API封装库
```python
import aliyun_api_py

# 创建API请求
request = aliyun_api_py.Api(access_key_id, access_key_secret, http_method, host, uri, x_acs_action, x_acs_version,algorithm)
request.param["your-param"] = "sth"
request.body["your-body"] = "sth"
print(request.exec())
```
`access_key_id`：

`access_key_secret`：

`http_method`：

`host`：

`uri`：

`x_acs_action`：

`x_acs_version`：

`algorithm`：

更多参数信息详见[请求结构和签名机制](https://help.aliyun.com/zh/sdk/product-overview/v3-request-structure-and-signature)
## 使用SDK
**目前SDK随缘更新，碰到自己需要的API可能会随手写个SDK方便调用**

API相关信息详见[阿里云API文档](https://api.aliyun.com/document)
```python
import aliyun_api_py

# 调用请求函数（以重启ECS为例）
request = aliyun_api_py.Ecs(access_key_id, access_key_secret, host)
print(request.reboot_instance(instance_id, force_stop, dry_run))
```
### ECS
`ecs.reboot_instance(instance_id, force_stop, dry_run)`：重启ECS实例