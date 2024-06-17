<img width="843" alt="image" src="https://github.com/winglang/wingification-image-resize/assets/1727147/dadc05b6-b146-415a-a910-696212ecfacd">


In this phase we are going to focus on getting the application to work using python Lambda (`bring python`) with minimal 


## Compromises

- The Bucket doesn't directly triggers the SQS, instead it triggers Lambda directly (we don't need the SQS queue for this phase)
- No Lambda Layers (requirements.txt with Pillow)

## WTF moments 
- No bucket name (https://github.com/winglang/wing/issues/6725)
- No ability to create a folder 
- No Queue name (https://github.com/winglang/wing/issues/6727)
- No way to download a file from a bucket in binary mode
