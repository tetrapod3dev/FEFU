package com.cloud.service;

import java.util.List;

import com.cloud.domain.CampaignDto;

public interface CampaignService {

	public List<CampaignDto> findAll(String campaignType, int pageNo, String type, String content);
	public List<String> findTagByNo(int no);
	public CampaignDto findDetail(int no);
	public int insertCampaign(CampaignDto dto);
	public int updateCampaign(CampaignDto dto);
	public int deleteCampaign(int no);
}
