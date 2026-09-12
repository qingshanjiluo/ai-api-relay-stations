#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI API 中转站批量搜集脚本
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re

def search_bing(query, count=10):
    """搜索 Bing 并返回结果"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    results = []
    url = f"https://www.bing.com/search?q={query}&count={count}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取搜索结果
        for item in soup.find_all('li', class_='b_algo'):
            title_elem = item.find('h2')
            link_elem = item.find('a')
            snippet_elem = item.find('p')
            
            if title_elem and link_elem:
                title = title_elem.get_text(strip=True)
                link = link_elem.get('href', '')
                snippet = snippet_elem.get_text(strip=True) if snippet_elem else ''
                
                results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })
                
    except Exception as e:
        print(f"搜索失败: {e}")
    
    return results

def extract_station_info(text):
    """从文本中提取中转站信息"""
    stations = []
    
    # 常见的中转站名称模式
    patterns = [
        r'([A-Za-z0-9\s]+(?:API|中转|中转站|代理|Relay|Gateway))',
        r'([A-Za-z0-9]+\.(?:ai|com|cn|io|net|org))',
        r'(?:名称|Name)[：:]\s*([^\n]+)',
        r'(?:网址|Website|URL)[：:]\s*([^\n]+)',
        r'(?:倍率|Rate)[：:]\s*([^\n]+)',
        r'(?:模型|Model)[：:]\s*([^\n]+)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            stations.extend(matches)
    
    return list(set(stations))

def main():
    """主函数"""
    print("开始搜集 AI API 中转站信息...")
    
    # 搜索关键词列表
    search_queries = [
        "中转站 倍率 OpenAI Claude",
        "AI API 中转 推荐",
        "OpenAI 中转 倍率",
        "Claude 中转 倍率",
        "GPT 中转 倍率",
        "API 中转 列表",
        "中转站 导航",
        "AI 中转站 排行榜"
    ]
    
    all_stations = []
    
    for query in search_queries:
        print(f"\n搜索: {query}")
        results = search_bing(query, count=20)
        
        for result in results:
            print(f"  标题: {result['title']}")
            print(f"  链接: {result['link']}")
            
            # 提取中转站信息
            stations = extract_station_info(result['title'] + ' ' + result['snippet'])
            all_stations.extend(stations)
            
            time.sleep(1)  # 避免请求过快
    
    # 去重
    unique_stations = list(set(all_stations))
    
    print(f"\n搜集到 {len(unique_stations)} 个中转站信息")
    
    # 保存到文件
    output_file = r"G:\皮皮\编程项目\07_工具与资料\中转站\scraped_stations.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for station in unique_stations:
            f.write(f"{station}\n")
    
    print(f"结果已保存到: {output_file}")
    
    # 同时保存为 JSON 格式
    json_file = r"G:\皮皮\编程项目\07_工具与资料\中转站\scraped_stations.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'search_queries': search_queries,
            'total_stations': len(unique_stations),
            'stations': unique_stations
        }, f, ensure_ascii=False, indent=2)
    
    print(f"JSON 结果已保存到: {json_file}")

if __name__ == "__main__":
    main()