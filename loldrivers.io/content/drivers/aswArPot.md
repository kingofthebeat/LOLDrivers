+++
description = "CVE-2022-26522, CVE-2022-26523: Both of these vulnerabilities were fixed in version 22.1."
title = "aswArPot.sys"
weight = 10
+++

# aswArPot.sys

#### Description

Avast’s “Anti Rootkit” driver (also used by AVG) has been found to be vulnerable to two high severity attacks that could potentially lead to privilege escalation by running code in the kernel from a non-administrator user.

- **Created**: 2023-01-09
- **Author**: Michael Haag
- **Acknowledgement**: MattNotMax | [@mattnotmax](https://twitter.com/@mattnotmax)

#### Command

```
sc.exe create aswSP_ArPot2 binPath= C:\windows\temp\aswArPot.sys type= kernel
sc.exe start aswSP_ArPot2 
```

#### Resources


<li><a href="{&#39; https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules&#39;}">{&#39; https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules&#39;}</a></li>





#### Binary Metadata

- Known Hashes: [4b5229b3250c8c08b98cb710d6c056144271de099a57ae09f5d2097fc41bd4f1](https://www.virustotal.com/gui/file/4b5229b3250c8c08b98cb710d6c056144271de099a57ae09f5d2097fc41bd4f1) 
- binary: 
- Verified: 
- Date: 2021-02-01 14:09:00
- Publisher: 
- Company: AVAST Software
- Description: Avast Anti Rootkit
- Product: Avast Antivirus

- ProductVersion: 
- FileVersion: 
- MachineType: 
- OriginalFilename: aswArPot.sys

[*source*](https://github.com/magicsword-io/LOLDrivers/tree/main/yaml/aswarpot.sys.yml)